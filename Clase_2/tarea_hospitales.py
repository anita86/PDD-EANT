# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 04:29:33 2021

@author: Ana
"""

import csv

with open('hospitales.csv', encoding='utf-8') as archivo_in, open('hospitales_salida.csv', 'w', newline='', encoding='utf-8') as archivo_out:
     entrada = csv.reader(archivo_in)
     salida = csv.writer(archivo_out, delimiter=';')
     next(entrada)#salta la primera linea de entrada
     salida.writerow(['latitude', 'longitude', 'name', 'label'])
     for linea in entrada:
         coordenadas = linea[0].strip('WK POINT ()')
         coordenadas = coordenadas.split(' ')
         # print(coordenadas)
         latitud = coordenadas[1]
         longitud = coordenadas[0]
         nombre = linea[2]
         direccion = linea[7]
         salida.writerow([latitud, longitud, nombre, direccion])

