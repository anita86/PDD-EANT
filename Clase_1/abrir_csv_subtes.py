# -*- coding: utf-8 -*-
"""
Created on Thu May 27 21:42:16 2021

@author: Ana
"""

archivo = open('subtes.csv', encoding='utf-8')

for linea in archivo:
    linea = linea.strip('\n')
    lista = linea.split(',')
    print(lista[2])
    