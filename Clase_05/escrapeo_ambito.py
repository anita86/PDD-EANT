# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 19:22:46 2021

@author: Ana
"""


from bs4 import BeautifulSoup as BS
import requests
import csv

url = 'https://www.ambito.com/'
respuesta = requests.get(url) 
respuesta.encoding = 'utf-8'
html = respuesta.text
dom = BS(html, features='html.parser')

etiquetas_class_title = dom.find_all(class_='title')

n = 0
tabla = [['Número', 'Titulo', 'Link']]

for etiqueta in etiquetas_class_title:
    link1 = etiqueta.a
    titulo = link1.string
    link2 = link1.get('href', 'No definido')
    n += 1
    print(str(n) + ' / ' + titulo + ' / ' + link2)
    fila = [n, titulo, link2]
    tabla.append(fila)
    
with open('noticias.csv', 'w', newline='') as file:
          writer = csv.writer(file, delimiter=';')
          writer.writerows(tabla)
          
#TAREA tabla mysql con datos de cuspide mas vendidos + titulo y precio 


