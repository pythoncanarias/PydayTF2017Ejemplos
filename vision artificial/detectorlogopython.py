#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 20:15:51 2017

@author: victor
"""

import cv2
import sys

import os
import csv



#script que a partir de una carpeta obtiene todas las imagenes y crea un csv con sus momentos de Hu

if len(sys.argv)<1:
    print("Uso humoments path")
    exit(1)
    

path = sys.argv[1]

if not os.path.exists(path):
    print("El parametro no es un fichero")
    exit(1)





image = cv2.imread(path,0)
data=cv2.HuMoments(cv2.moments(image)).flatten()
if(data[0]>0.001014):
     print(path+' es un logo de python')
else:
     print(path+' No es un logo de python')

    
