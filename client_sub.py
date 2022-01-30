import paho.mqtt.client as mqtt
import time
import json
import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="password",
    database="test1"
)

def insert_data(val):
    mycursor = mydb.cursor()
    sql = "insert into predictioninfo (Date, Time, lat, lon, pmval) VALUES (%s, %s, %s, %s, %s)"
    mycursor.execute(sql, val)
    mydb.commit()

def on_message(client, userdata, message):
    data = (message.payload.decode('utf-8'))
    data = json.loads(data)
    listdata = [data['Date'],data['Time'],data['lat'],data['lon'],data['pmval']]
    print(listdata)
    insert_data(listdata)

def on_connect(client, userdata, flags, rc): 
    print("Connected with result code {0}".format(str(rc))) 
    client.subscribe("pm2.5")

broker = '34.124.157.195'
client_name = 'Tong' + str(time.time())
client = mqtt.Client(client_name)
client.on_message = on_message
client.connect(broker)
client.loop_start()
client.subscribe('pm2.5')