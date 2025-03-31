import paho.mqtt.publish as publish

publish.single("paho/test/rpi-laptop", "fuck you", hostname="mqtt.eclipseprojects.io")