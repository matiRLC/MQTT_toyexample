import paho.mqtt.client as mqttClient
import time

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected
        Connected = True
    else:
        print("Connection failed")
 
def on_message(client, userdata, message):
    print "Message received: "  + message.payload
    print "message topic: " + message.topic

def on_log(client, userdata, level, buf):
	print("log: ", buf)

Connected = False  # connection status

# Broker information
broker_address= "m10.cloudmqtt.com"
port = 11017
user = "jjmdwcmw"
password = "raoJ0gQNFSVp"

# Client instance 
mqttc = mqttClient.Client()
mqttc.username_pw_set(user, password = password)
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.connect(broker_address, port = port)
# mqttc.on_log = on_log # DEBUG option

# Start loop
mqttc.loop_start()
 
# Wait for connection
while Connected != True:
    time.sleep(0.1)
 
mqttc.subscribe("python/test")
 
try:
    while True:
        time.sleep(1)
 
except KeyboardInterrupt:
    print "exiting"
    client.disconnect()
    client.loop_stop()


# ref: 
#	https://techtutorialsx.com/2017/04/23/python-subscribing-to-mqtt-topic/