# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 22:45:25 2021

@author: Ana
"""

from selenium import webdriver
from bs4 import BeautifulSoup as BS
from time import sleep

#Primero despliego todo el DOM
driver = webdriver.Chrome('C:/Users\Ana\Desktop\PDD EANT\chromedriver.exe')

driver.get('https://www.olx.com.ar/items/q-aspiradoras-auto')

script_js = """
let boton = document.querySelector('[data-aut-id="btnLoadMore"]')
if (boton) {
        boton.click()
        } 
else{
     return "No existe"
     }
"""
sleep(3)

while driver.execute_script(script_js) != "No existe": sleep(3)

sleep(3)

#Luego capturo la info deseada
html = driver.execute_script("return document.documentElement.outerHTML")
dom = BS(html, features='html.parser')
productos = dom.find_all(class_="IKo3_")
print("Cantidad de productos: ", len(productos))
for producto in productos:
    precio = producto.find(class_="_89yzn").string
    precio = producto.find(class_="2tW1I").string
    print(titulo, '-', precio)


    

