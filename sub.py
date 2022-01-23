import paho.mqtt.client as mqtt
import time
import json

def on_message(client1, userdata, message):
    print(message.payload)


broker = '34.124.157.195'

client2 = mqtt.Client('Subsciber')
client2.connect(broker)
client2.on_message = on_message

client2.subscribe('pm2.5')

client2.loop_forever()
