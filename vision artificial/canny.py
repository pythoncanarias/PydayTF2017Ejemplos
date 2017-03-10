#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 20:01:45 2017

@author: victor
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

file= '/Users/victor/Documents/pythoncanarias/ejemplos/pythonlogo.png'
img = cv2.imread(file,cv2.IMREAD_COLOR)
edges = cv2.Canny(img,100,200)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()