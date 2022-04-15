# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 00:24:05 2022

@author: Franklin
"""
#https://github.com/serengil/deepface

from deepface import DeepFace
import cv2
import os
import pandas as pd
#import matplotlib.pyplot as plt

input_images_path = "D:/utp/IA/capturas"
files_names = os.listdir(input_images_path)
#print(files_names)

dataframe = []

def limpiar_data():
    for i in files_names:
        print(i)
        image_path = input_images_path +"/"+ i
        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        value = cv2.Laplacian(gray, cv2.CV_64F).var()
        if value < 150:
            os.remove(image_path)

def procesar_data():
    for i in files_names:
        print(i)
        image_path = input_images_path +"/"+ i
        #img = cv2.imread(image_path)
        #imgplot = plt.imshow(img)
        obj = DeepFace.analyze(img_path = image_path, actions = ['age', 'gender', 'race', 'emotion'])
        print(obj["age"]," years old ",obj["dominant_race"]," ",obj["dominant_emotion"]," ", obj["gender"])
        dataframe.append([obj["age"],obj["dominant_race"],obj["dominant_emotion"],obj["gender"],i,i[0:36]])

def guardar_data():
   df_rrss = pd.DataFrame(dataframe,columns = ['edad','raza dominante','emocion','genero','archivo','id'])
   df_rrss.to_csv('D:/utp/IA/data_rrss.csv',index=False,sep=';')

#limpiar_data()
procesar_data()
guardar_data()