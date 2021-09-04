# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 22:48:09 2021

@author: Ana
"""
import requests

url = 'https://eant.tech/cursos/recursos/peliculas.csv'
respuesta = requests.get(url) 
contenido = respuesta.text
with open('pelis.csv', 'w') as pelis:
    pelis.write(contenido)