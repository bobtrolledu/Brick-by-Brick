import paho.mqtt.publish as publish

def send_message(msg):
    publish.single("paho/test/rpi-laptop", msg, hostname="mqtt.eclipseprojects.io")