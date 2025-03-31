import paho.mqtt.client as mqtt

broker = "broker.hivemq.com"
topic = "test/pi-laptop"

client = mqtt.Client()

client.connect(broker, 1883, 60)

def send_message(message):
    client = mqtt.Client()

    client.connect(broker, 1883, 60)
    client.publish(topic, message)
    print("Message sent!")

    client.disconnect()

