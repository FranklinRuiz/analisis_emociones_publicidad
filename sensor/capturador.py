# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 18:43:56 2022

@author: Franklin
"""
#https://www.expansion.com/directivos/2016/05/10/5730f01fe2704e25178b461c.html
import paho.mqtt.client as mqtt
import cv2
import uuid
from datetime import datetime

def on_camara_capture():
    cap = cv2.VideoCapture(0)
    id = uuid.uuid4()
    numero = 1
    
    instanteInicial = datetime.now()    
    while True:
        leido, frame = cap.read()
        
        nombre_archivo = str(id)+"-"+str(numero)
        numero = numero + 1
        
        if leido == True:
            nombre_foto = "D:/utp/IA/capturas/"+nombre_archivo + ".png"
            cv2.imwrite(nombre_foto, frame)
            print("Foto tomada correctamente con el nombre {}".format(nombre_foto))
        else:
            print("Error al acceder a la cámara")
            cap.release()
        
        # al final de la partida
        instanteFinal = datetime.now()
        tiempo = instanteFinal - instanteInicial # Devuelve un objeto timedelta
        segundos = tiempo.seconds
        print(segundos)    
        if segundos >=6:
            break
    
    cap.release()
    
on_camara_capture()
    
#Connection success callback
def on_connect(client, userdata, flags, rc):
    print('Connected with result code '+str(rc))
    client.subscribe('utp/sensor')

# Message receiving callback
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    if msg.payload.decode("utf-8") == 'ON':
        on_camara_capture()


client = mqtt.Client()

# Specify callback function
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set("franklin", "EXAMPLE_PASSWORD")

# Establish a connection
client.connect('192.168.1.62', 1883, 60)
# Publish a message
#client.publish('emqtt',payload='Hello World',qos=0)

client.loop_forever()

