# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 00:54:17 2021

@author: Ana
"""

from bs4 import BeautifulSoup as BS
import requests

url = 'https://www.cuspide.com/cienmasvendidos'
respuesta = requests.get(url) 
respuesta.encoding = 'utf-8'
html = respuesta.text

dom = BS(html, features='html.parser')

articulos = dom.find_all('article')

for articulo in articulos:
    print(articulo .figure.div.a['title'])

print("Solo el top 10")
for i in range(len(articulos)):
    print(i+1, articulos[i].figure.div.a['title'])





