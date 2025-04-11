import paho.mqtt.publish as publish

publish.single("paho/test/topic", "fuck you", hostname="mqtt.eclipseprojects.io")