#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script que muestra todas las imagenes de una carpeta

@author: victor
"""

import fnmatch
import os

images = ['*.jpg', '*.jpeg', '*.png', '*.tif', '*.tiff']
matches = []

for root, dirnames, filenames in os.walk('/Users/Victor/Desktop'):
    for extensions in images:
        for filename in fnmatch.filter(filenames, extensions):
            matches.append(os.path.join(root, filename))
print(matches)