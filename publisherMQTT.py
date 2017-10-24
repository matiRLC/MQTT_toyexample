import paho.mqtt.client as mqttClient
import time
import random
 
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print "Connected to broker"
        global Connected
        Connected = True
    else:
        print("Connection failed")
 
def on_publish(client, userdata, mid):
    print "Message was published!\n"

Connected = False # connection status

# Broker information
broker_address= "m10.cloudmqtt.com"
port = 11017
user = "jjmdwcmw"
password = "raoJ0gQNFSVp"
    
# Client instance
mqttc = mqttClient.Client()
mqttc.username_pw_set(user, password = password)
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.connect(broker_address, port = port)
# mqttc.on_log = on_log # DEBUG option

# Start lop     
mqttc.loop_start()

# Wait for connection
while Connected != True:
    time.sleep(0.1)
 
try:
    while True:
        # value = raw_input('Enter the message: ')
        # simulating Temperature sensor (that changes draaastically)
        value = random.randint(60, 80)
        mqttc.publish("python/test", value)
        # with sampling rate of 0.5Hz
        time.sleep(2)

except KeyboardInterrupt:
    mqttc.disconnect()
    mqttc.loop_stop()
