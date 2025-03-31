import paho.mqtt.client as mqtt
import stepper_control as step_c
import servo_control as servo_c
import feeder_control as fc
import time

complete = True
coords_queue = []

def move_box(coords_x, coords_y):
    global complete
    complete = False
    print(f"Moving to coordinates: x={coords_x}, y={coords_y}")
    step_c.setup()
    step_c.go_to_box(coords_x, coords_y)
    servo_c.open_close()
    step_c.go_to_box(0, 0)
    step_c.reset()
    print("Movement complete.")
    complete = True

def on_message(client, userdata, msg):
    global coords_queue
    try:
        coords = msg.payload.decode().split(",")
        x = int(coords[0])
        y = int(coords[1])
        print(f"Received coordinates: x={x}, y={y}")
        coords_queue.append((x, y))
    except (ValueError, IndexError) as e:
        print(f"Invalid message received: {msg.payload.decode()} - Error: {e}")

# Configure MQTT client
client = mqtt.Client()
client.on_message = on_message
client.connect("mqtt.eclipseprojects.io", 1883, 60)
client.subscribe("paho/test/rpi-laptop")

print("Listening for messages...")

# Main loop to handle MQTT and stepper control
while True:
    client.loop(timeout=0.1)  # Process MQTT messages
    if complete and coords_queue:
        x, y = coords_queue.pop(0)
        move_box(x, y)
    if complete:
        fc.pulse(1)
    time.sleep(0.01)  # Prevent CPU overuse
