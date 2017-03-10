#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 16:50:41 2017

@author: victor
"""

from http import client

h1 = client.HTTPConnection('www.google.es',80)
h1.request('GET','/')
conn = h1.getresponse()
print(str(conn.status)+ ' '+conn.reason)
print('--------')
print(conn.read())