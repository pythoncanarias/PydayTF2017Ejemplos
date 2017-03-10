#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 20:15:51 2017

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

#script que a partir de una carpeta obtiene todas las imagenes y crea un csv con sus momentos de Hu

if len(sys.argv)<1:
    print("Uso humoments path")
    exit(1)
    

path = sys.argv[1]

if not os.path.isdir(path):
    print("El parametro no es un directorio")
    exit(1)

imagenes = obtenerimagenes(path)

with open('huMoments.csv', 'wb') as csvfile:
    for pathimage in imagenes:
        image = cv2.imread(pathimage,0)
        data=cv2.HuMoments(cv2.moments(image)).flatten()
        spamwriter = csv.writer(csvfile)
        spamwriter.writerow(data)

    
