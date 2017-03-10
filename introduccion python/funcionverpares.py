#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
funcion que muestra los primeros N pares donde N es un parametro

@author: victor
"""

def verpares(numpares):
    for i in range(0,numpares):
        if (i%2)==0:
            print(i)
            

verpares(100)