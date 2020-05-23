# -*- coding: utf-8 -*-
"""
Created on Wed May 20 09:05:09 2020

@author: sarad
"""

#Generation of QR code
#STEP 1: Prepare the data in the form of 'vCard' data structure
#STEP 2: Convert 'vCard' into 'QRCode' data structure
#STEP 3: Save it as image

import segno
from segno import helpers

#STEP 1: Prepare the data in the form of 'vCard' data structure
#Reference:
#https://pypi.org/project/segno/
#https://readthedocs.org/projects/segno/downloads/pdf/0.3.0/
vcard = helpers.make_vcard_data(name='EFG;ABCD', displayname='Abcd Efg', email='efg@example.org', phone='+1234567890', url='http://www.abcd.org')
print(vcard)

#STEP 2: Convert 'vCard' into 'QRCode' data structure
qr = segno.make(vcard)

#STEP 3: Save it as image
qr.save('abcd.png',scale=4)

#Load and display the QRCode image
#We use 'openCV' library for loading image, and
#For displaying the image we use 'matplotlib' library

import cv2
from matplotlib import pyplot as plt
import numpy as np

image = cv2.imread("abcd.png")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# as opencv loads in BGR format by default, we want to show it in RGB.
plt.show()

#Decode the QR code image
#STEP 1: Decode it using 'pyzbar' library
#STEP 2: Extract the data from the object returned by this library
#STEP 3: Present the extracted data in a format suitable of easy interpretation by humans

import pyzbar.pyzbar as pyzbar
import re

#STEP 1: Understanding the object returned by pyzbar
#'pyzbar' returns an object which consists of several elements
#Among them we are interested mostly in 'data' element
decodedObjects = pyzbar.decode(image)
print(decodedObjects)

for obj in decodedObjects:
    typ = obj.type
    data = obj.data
    rect = obj.rect
    poly = obj.polygon
print('Type: ', typ)
print('Data: ', data)
print('Rectangle: ', rect)
print('Polygon: ', poly)

#STEP 2: Converting the 'data' into string type
#'data' is in byte format i.e., in ASCII format
#Reference: https://theasciicode.com.ar/
#It has to be converted into 'utf-8' format
#Reference: https://www.geeksforgeeks.org/python-strings-decode-method/

data1 = data.decode('utf-8')
data2=re.split(r'[\n]',data1)

emails = []
urls = []
for line in data2:
    #print(line)
    line = re.split(r'[\:]',line,1) # the third argument '1' is necessary, figure out why?
    #print(line)
    if line[0]=='EMAIL':
        emails.append(line[1][:-1]) # figure out why [:-1] is necessary 
    if line[0]=='URL':
        urls.append(line[1][:-1])
print(emails)
print(urls)










