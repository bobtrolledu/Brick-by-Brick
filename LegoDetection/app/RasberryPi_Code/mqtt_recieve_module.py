import paho.mqtt.subscribe as subscribe

msg = subscribe.simple("paho/test/rpi-laptop", hostname="mqtt.eclipseprojects.io")
print("%s %s" % (msg.topic, msg.payload))
    