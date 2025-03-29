from flask import jsonify, render_template, Response, request, redirect, url_for
from flask_socketio import SocketIO
from flask_cors import CORS
import requests
import cv2
import json
import tempfile
import os
import datetime as DT 
import numpy as np
from app import app, db
from app.lego import LegoPiece

API_URL = "https://api.brickognize.com/predict/"
CAMERA_SELECT = 0 # change if needed; 0 normally works
API_SEND_INTERVAL = 1.5 # i don't recommend anything lower than 1 second cause the api can't keep up

COLOR_RANGES = { # color ranges for OpenCV color detection model
    'Red': [np.array([0, 100, 100]), np.array([10, 255, 255])],
    'Orange': [np.array([10, 100, 100]), np.array([30, 255, 255])],
    'Yellow': [np.array([25, 100, 100]), np.array([45, 255, 255])],
    'Green': [np.array([50, 100, 50]), np.array([90, 255, 255])],
    'Blue': [np.array([90, 100, 100]), np.array([110, 255, 255])],
    'Purple': [np.array([140, 100, 100]), np.array([170, 255, 255])],
    'Brown': [np.array([10, 50, 50]), np.array([20, 255, 100])],
    'Grey/Black': [np.array([0, 0, 0]), np.array([180, 50, 200])],
    'White': [np.array([0, 0, 200]), np.array([180, 50, 255])]
}

CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

last_called = DT.datetime.now()
boundingbox = None

# right now the program will detect the brick every set interval;
# should most likely change the behavior to better suit the build
def brick_type_detect(image):
    global last_called, boundingbox

    if (DT.datetime.now() - last_called).total_seconds() >= API_SEND_INTERVAL:
        try:
            # writes a jpeg to temp to upload to API and display as live feed
            with tempfile.TemporaryDirectory() as temp_dir:
                temp_img_path = os.path.join(temp_dir, "brick.jpg")
                cv2.imwrite(temp_img_path, image)
                response = requests.post(API_URL, headers={'accept': 'application/json'}, files={'query_image': (temp_img_path, open(temp_img_path, 'rb'), 'image/jpeg')})

            data = json.loads(response.content)
            if 'items' not in data or not data['items']: # if brickify fails to detect
                socketio.emit('update_info', {'id': 'N/A', 'name': 'N/A', 'confidence': '-1', 'color': 'N/A'})
                return
            boundingbox = data['bounding_box']
            brickid = data['items'][0]['id']
            name = data['items'][0]['name']
            confidence = data['bounding_box']['score'] * 100
            last_called = DT.datetime.now()

            # calculates top-left and bot-right coordinates of bounding box for detected lego piece
            l, r, u, d = boundingbox['left'], boundingbox['right'], boundingbox['upper'], boundingbox['lower']
            iw, ih = boundingbox['image_width'], boundingbox['image_height']
            fh, fw, _ = image.shape
            top_left = (int(l/iw * fw), int(u/ih * fh))
            bottom_right = (int(r/iw * fw), int(d/ih * fh))
            color, _ = get_primary_color(image, top_left, bottom_right)

            add_to_database(name, color, brickid, 1)

            # dynamic update for info describing live camera feed
            socketio.emit('update_info', {'id': brickid, 'name': name, 'confidence': round(confidence, 2), 'color': color})
            return top_left, bottom_right
        except requests.exceptions.RequestException as e:
            return {"status": "DOWN", "message": str(e)}

# returns primary color from image given a bounding box
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

detection_enabled = True

@app.route('/api/toggle_detection', methods=['POST'])
def toggle_detection():
    global detection_enabled
    data = request.json
    detection_enabled = data.get('detecting', True)
    return jsonify({"status": "success", "detecting": detection_enabled})

@app.route('/api/detection_status')
def get_detection_status():
    return jsonify({"detecting": detection_enabled})

# handle image processing
def process_frame(frame):
    if detection_enabled and boundingbox:
        l, r, u, d = boundingbox['left'], boundingbox['right'], boundingbox['upper'], boundingbox['lower']
        iw, ih = boundingbox['image_width'], boundingbox['image_height']
        fh, fw, _ = frame.shape
        top_left = (int(l/iw * fw), int(u/ih * fh))
        bottom_right = (int(r/iw * fw), int(d/ih * fh))
        cv2.rectangle(frame, top_left, bottom_right, (255, 0, 0), 2)
    return frame

# primary loop: displays the camera feed
def generate_frames():
    camera = cv2.VideoCapture(CAMERA_SELECT)
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            if detection_enabled:
                frame_copy = frame.copy()
                socketio.start_background_task(brick_type_detect, frame_copy)
            frame = process_frame(frame)
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route("/video") # streams video
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace;boundary=frame')

# route for getting all entries in db
@app.route('/api/get_pieces')
def get_pieces():
    with app.app_context():
        pieces = db.session.execute(db.select(LegoPiece).order_by(LegoPiece.name)).scalars()
        return jsonify([{
            "id": p.id,
            "name": p.name,
            "color": p.color,
            "brickid": p.brickid,
            "quantity": p.quantity
        } for p in pieces])

# route for adding a db entry
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

# calls socket to refresh list items in list.html
def refresh_list():
    with app.app_context():
        pieces = db.session.execute(db.select(LegoPiece).order_by(LegoPiece.name)).scalars()
        pieces_data = [{"id": p.id, "name": p.name, "color": p.color, "brickid": p.brickid, "quantity": p.quantity} for p in pieces]
        socketio.emit('refresh-list', {'pieces': pieces_data})

# adds lego piece to database
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

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)