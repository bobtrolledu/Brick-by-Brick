import time
import requests
import json
import tempfile
import os
import numpy as np
import cv2
from flask import jsonify, Response, request
from flask_socketio import SocketIO
from flask_cors import CORS
from app import app, db
from app.lego import LegoPiece
from app.codes.mqtt_send_test import send_message
import paho.mqtt.client as mqtt

API_URL = "https://api.brickognize.com/predict/"
CAMERA_SELECT = 1  # change if needed; 0 normally works
API_SEND_INTERVAL = 1.5  # i don't recommend anything lower than 1 second cause the api can't keep up
BINS = {
    'Red': '0,0',
    'Orange': '0,1',
    'Yellow': '0,2',
    'Green': '1,0',
    'Blue': '1,1',
    'Purple': '1,2',
    'Brown': '2,0',
    'Grey/Black': '2,1',
    'White': '2,2'
}
COLOR_RANGES = {
    'Red': [np.array([0, 120, 70]), np.array([10, 255, 255])],
    'Orange': [np.array([11, 150, 100]), np.array([25, 255, 255])],
    'Yellow': [np.array([26, 150, 150]), np.array([35, 255, 255])],
    'Green': [np.array([36, 100, 100]), np.array([85, 255, 255])],
    'Blue': [np.array([86, 150, 100]), np.array([125, 255, 255])],
    'Purple': [np.array([126, 100, 100]), np.array([160, 255, 255])],
    'Brown': [np.array([10, 80, 20]), np.array([20, 255, 150])],
    'Grey/Black': [np.array([0, 0, 0]), np.array([180, 50, 100])],
    'White': [np.array([0, 0, 200]), np.array([180, 30, 255])]
}

CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

boundingbox = None
response_received = True  # Initially set to True to allow the first API call
movement_in_progress = False
toggle_detect = False
task_in_progress = False

# MQTT callback to handle movement completion
def on_message(client, userdata, msg):
    global movement_in_progress, response_received
    payload = msg.payload.decode()
    if payload == "done":
        print("Movement complete, resuming detection.")
        movement_in_progress = False
        response_received = True
    else:
        print(f"Movement in progress: {payload}")
        movement_in_progress = True

client = mqtt.Client()
client.on_message = on_message
client.connect("mqtt.eclipseprojects.io", 1883, 60)
client.subscribe("paho/test/rpi-laptop")
client.loop_start()

# Function to detect brick type via API
def brick_type_detect(image):
    global boundingbox, movement_in_progress, response_received, task_in_progress
    try:
        if task_in_progress:  # Check if a task is already running
            return  # Skip if the task is already running

        task_in_progress = True  # Mark that a task is running

        # Write a JPEG to temp to upload to API and display as live feed
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_img_path = os.path.join(temp_dir, "brick.jpg")
            cv2.imwrite(temp_img_path, image)
            print(f"Image saved at {temp_img_path}")  # Debugging line

            # Send the image to the Brickognize API
            response = requests.post(API_URL, headers={'accept': 'application/json'},
                                     files={'query_image': (temp_img_path, open(temp_img_path, 'rb'), 'image/jpeg')},
                                     timeout=10)

            print(f"API response status code: {response.status_code}")  # Debugging line

            # Parse API response
            data = response.json()
            print(f"API response data: {data}")  # Debugging line
            if 'items' not in data or not data['items'] or movement_in_progress or data['items'][-1]['score'] * 100 < 65.0:  # if brickify fails to detect
                socketio.emit('update_info', {'id': 'N/A', 'name': 'N/A', 'confidence': '-1', 'color': 'N/A'})
                task_in_progress = False  # Reset the task flag
                return

            # Extract the bounding box and brick details
            boundingbox = data['bounding_box']
            brickid = data['items'][0]['id']
            name = data['items'][0]['name']
            confidence = data['items'][-1]['score'] * 100

            # Calculate the top-left and bottom-right coordinates of the bounding box for the detected Lego piece
            l, r, u, d = boundingbox['left'], boundingbox['right'], boundingbox['upper'], boundingbox['lower']
            iw, ih = boundingbox['image_width'], boundingbox['image_height']
            fh, fw, _ = image.shape
            top_left = (int(l / iw * fw), int(u / ih * fh))
            bottom_right = (int(r / iw * fw), int(d / ih * fh))

            # Get the primary color of the detected brick
            color, _ = get_primary_color(image, top_left, bottom_right)

            # Add to database and send message to sort the piece into the corresponding bin
            add_to_database(name, color, brickid, 1)
            print("sent " + BINS[color])
            send_message(BINS[color])
            movement_in_progress = True
            response_received = False
            # Emit a dynamic update with live camera feed information
            socketio.emit('update_info',
                          {'id': brickid, 'name': name, 'confidence': round(confidence, 2), 'color': color})

            task_in_progress = False  # Reset the task flag after completion
            return top_left, bottom_right
    except requests.exceptions.RequestException as e:
        task_in_progress = False  # Reset the task flag in case of an exception
        return {"status": "DOWN", "message": str(e)}


# Function to get the primary color of the brick
def get_primary_color(image, top_left, bottom_right):
    x1, y1 = top_left
    x2, y2 = bottom_right
    roi = image[y1:y2, x1:x2]
    hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    pixel_counts = {}
    for color, (lower, upper) in COLOR_RANGES.items():
        mask = cv2.inRange(hsv_roi, lower, upper)
        count = cv2.countNonZero(mask)
        pixel_counts[color] = count

    most_prevalent = max(pixel_counts, key=pixel_counts.get)
    max_count = pixel_counts[most_prevalent]

    return most_prevalent, max_count

# Flask route to toggle detection
@app.route('/api/toggle_detection', methods=['POST'])
def toggle_detection():
    global toggle_detect
    data = request.json
    toggle_detect = data.get('detecting', False)
    return jsonify({"status": "success", "detecting": toggle_detect})

# Flask route to check detection status
@app.route('/api/detection_status')
def get_detection_status():
    return jsonify({"detecting": toggle_detect})

# Function to process frames and detect bricks
def process_frame(frame):
    if not movement_in_progress and boundingbox and toggle_detect:
        l, r, u, d = boundingbox['left'], boundingbox['right'], boundingbox['upper'], boundingbox['lower']
        iw, ih = boundingbox['image_width'], boundingbox['image_height']
        fh, fw, _ = frame.shape
        top_left = (int(l/iw * fw), int(u/ih * fh))
        bottom_right = (int(r/iw * fw), int(d/ih * fh))
        cv2.rectangle(frame, top_left, bottom_right, (255, 0, 0), 2)
    return frame

# Frame generation function that checks the API call interval
# Frame generation function that checks the API call interval
def generate_frames():
    global response_received
    last_api_call_time = time.time()  # Timestamp for the last API call
    camera = cv2.VideoCapture(CAMERA_SELECT)
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    camera.set(cv2.CAP_PROP_FPS, 24)

    while True:
        success, frame = camera.read()
        if not success:
            break

        current_time = time.time()

        # Check if API call can be made
        if not movement_in_progress and not task_in_progress:  # Ensure no task is running
            if (current_time - last_api_call_time) >= API_SEND_INTERVAL and toggle_detect and response_received:  # API call interval check
                # Only make the API call if the interval has passed and no task is in progress
                last_api_call_time = current_time  # Update last API call time
                #frame_copy = frame.copy()
                #frame_copy = cv2.resize(frame_copy, (1280, 720), interpolation=cv2.INTER_AREA)

                socketio.start_background_task(brick_type_detect, frame)  # Call API in background

        frame = process_frame(frame)
        ret, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 85])
        frame = buffer.tobytes()
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# Route for streaming video
@app.route("/video")
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace;boundary=frame')

# Add a new Lego piece to the database
def add_to_database(name, color, brickid, quantity):
    with app.app_context():
        piece = db.session.query(LegoPiece).filter_by(brickid=brickid, color=color).first()
        if piece:
            piece.quantity += quantity
        else:
            new_piece = LegoPiece(
                name=name,
                color=color,
                brickid=brickid,
                quantity=quantity
            )
            db.session.add(new_piece)
        db.session.commit()
        refresh_list()

# Refresh the list of Lego pieces
def refresh_list():
    with app.app_context():
        pieces = db.session.execute(db.select(LegoPiece).order_by(LegoPiece.name)).scalars()
        pieces_data = [{"id": p.id, "name": p.name, "color": p.color, "brickid": p.brickid, "quantity": p.quantity} for p in pieces]
        socketio.emit('refresh-list', {'pieces': pieces_data})

@app.route('/api/add', methods=['POST'])
def add_piece():
    try:
        data = request.json
        name = data['name']
        color = data['color']
        brickid = data['brickid']
        quantity = int(data['quantity'])
        add_to_database(name, color, brickid, quantity)
        return jsonify({"message": "Success"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# route for deleting specific db entry
@app.route('/api/delete/<int:id>', methods=['DELETE'])
def delete_piece(id):
    try:
        piece = db.session.get(LegoPiece, id)
        if piece:
            db.session.delete(piece)
            db.session.commit()
            refresh_list()
            return '', 204
        return jsonify({"error": "Piece not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# route for deleting everything from db
@app.route('/api/delete_all', methods=['POST'])
def delete_all():
    try:
        pieces = db.session.execute(db.select(LegoPiece)).scalars()
        for piece in pieces:
            db.session.delete(piece)
        db.session.commit()
        refresh_list()
        return '', 204
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
