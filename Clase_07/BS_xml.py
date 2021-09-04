# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 19:15:43 2021

@author: Ana
"""

from bs4 import BeautifulSoup as BS

archivo = open('books.xml', encoding = 'utf-8')
xml = BS(archivo, features='lxml')

fechas = xml.find_all('publishdate')
precios = xml.find_all('price')
for i in range(len(fechas)):
    print("Fecha de publicación: ", fechas[i].text)
    print("Precio: ", precios[i].text)
