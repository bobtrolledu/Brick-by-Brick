import paho.mqtt.client as mqtt
import stepper_control
broker = "broker.hivemq.com"
topic = "test/pi-laptop"

def on_message(client, userdata, msg):
    print(f"Recived: {msg.payload.decode()} on topic {msg.topic}")
    coords = (msg.payload.decode()).split(",")
    x = int(coords[0])
    y = int(coords[1])
    move_box(x,y)

def move_box(coords_x, coords_y):
    test.setup()
    test.go_to_box(coords_x, coords_y)
    test.go_to_box(0,0)
    test.reset

client = mqtt.Client()
client.on_message = on_message

client.connect(broker, 1883, 60)
client.subscribe(topic)

print("listening for messages... Press ctrl+c to exit")
client.loop_forever() 
 
#if __name__ == "__main__":
    