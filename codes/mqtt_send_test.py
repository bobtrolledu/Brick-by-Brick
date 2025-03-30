import paho.mqtt.client as mqtt

broker = "broker.hivemq.com"
topic = "test/pi-laptop"

client = mqtt.Client()

client.connect(broker, 1883, 60)

while True:
    message = input("Enter message to send: ")
    client.publish(topic, message)
    print("Message sent!")
    if message.lower() == "exit":
        break

client.disconnect()

def send_message(topic, broker, message):
    client = mqtt.Client()

    client.connect(broker, 1883, 60)
    client.publish(topic, message)
    print("Message sent!")

    client.disconnect()

