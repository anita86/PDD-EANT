# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 22:48:09 2021

@author: Ana
"""
import requests
import csv
from io import StringIO #parsea en estructuras mas reconocibles


url = 'https://eant.tech/cursos/recursos/peliculas.csv'
respuesta = requests.get(url) 
contenido = respuesta.text
file = StringIO(contenido)
objeto_csv = csv.reader(file)

with open('pelis2.csv', 'w') as pelis:
    for linea in objeto_csv:
        fila = ','.join([linea[0], linea[2], linea[1]])
        pelis.write(fila + '\n')