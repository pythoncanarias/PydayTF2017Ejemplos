# -*- coding: utf-8 -*-
"""
Borrarvocales. Este script python borra las vocales de una frase.

This is a temporary script file.
"""

frase='Hola a todos; esto es python'
vocales=['a','e','i','o','u']

for letra in frase:
    if letra in vocales:
        frase=frase.replace(letra,'')
        
print(frase)