# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 22:48:09 2021

@author: Ana
"""
import requests
import csv
from io import StringIO #parsea en estructuras mas reconocibles


url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSRob-CS0sV1r_e3-e3nSO4Czrice5ApxDNIlRjXivZbAGR-_NNXJpdWl5MJoG1wrOVCtwJZ40asxct/pub?gid=0&single=true&output=csv'

respuesta = requests.get(url) 
contenido = respuesta.text
file = StringIO(contenido)
objeto_csv = csv.reader(file)

with open('pelis_google.csv', 'w') as pelis:
    for linea in objeto_csv:
        fila = ','.join([linea[0], linea[1], linea[2]])
        pelis.write(fila + '\n')