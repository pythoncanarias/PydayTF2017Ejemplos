#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
obtiene una imagen a partir de una imagen solo las partes en amarillo.

@author: victor
"""

import cv2
import numpy as np

file= '/Users/victor/Documents/pythoncanarias/ejemplos/pythonlogo.png'

image=cv2.imread(file,cv2.IMREAD_COLOR)
cv2.imshow('Original',image)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

amarillo_bajo = np.array([255,255,0])
amarillo_alto = np.array([255,255,255])


threshold=cv2.inRange(image, amarillo_bajo, amarillo_alto)

cv2.imshow('Image hsv',hsv)
cv2.imshow('Image Threshold', threshold)


cv2.waitKey(0)

cv2.destroyAllWindows()