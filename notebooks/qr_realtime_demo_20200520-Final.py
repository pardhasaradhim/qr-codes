# -*- coding: utf-8 -*-
"""
Created on Wed May 20 09:11:18 2020

@author: sarad
"""

import cv2
from matplotlib import pyplot as plt
import numpy as np
import pyzbar.pyzbar as pyzbar
import re

#Extraction of data from QR code image in real time

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

while True:
    _, frame = cap.read()
 
    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        #print("Data", obj.data)
        data = obj.data
        data1 = data.decode('utf-8')
        data2=re.split(r'[\n]',data1)
        #print(data2)
        emails = []
        urls = []
        for line in data2:
            #print(line)
            line = re.split(r'[\:]',line,1)
            #print(line)
            if line[0]=='EMAIL':
                emails.append(line[1][:-1])
            if line[0]=='URL':
                urls.append(line[1][:-1])
        #print(emails,urls)
        cv2.putText(frame, str(emails), (50, 50), font, 2, (255, 0, 0), 3)

    #cv2.putText(frame, str('Hi'),(50, 50), font, 2, (255, 0, 0), 3)
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(30) & 0xff
    if key == 27 or cv2.getWindowProperty('Frame', 0)<0:
        break
cv2.destroyAllWindows()
cap.release()
