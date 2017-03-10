#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 20:44:01 2017

@author: victor
"""

import cv2
import sys
import fnmatch
import os
import csv

def obtenerimagenes(path):
    images = ['*.jpg', '*.jpeg', '*.png', '*.tif', '*.tiff']
    matches = []
    for root, dirnames, filenames in os.walk(path):
        for extensions in images:
            for filename in fnmatch.filter(filenames, extensions):
                matches.append(os.path.join(root, filename))
    return matches

if len(sys.argv)<2:
    print("Uso humoments path")
    exit(1)
    

path = sys.argv[1]
path2= sys.argv[2]

if not os.path.isdir(path):
    print("El parametro1 no es un directorio")
    exit(1)
    
if not os.path.isdir(path2):
    os.mkdir(path2)
    
imagenes = obtenerimagenes(path)
i=1
for pathimagen in imagenes:
    image = cv2.imread(pathimagen,cv2.IMREAD_COLOR)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    print(path2+pathimagen)
    cv2.imwrite(path2+'imagen'+str(i)+'.png',hsv)
    i+=1

