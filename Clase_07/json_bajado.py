# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 20:24:19 2021

@author: Ana
"""
import csv
import json
from pprint import pprint
import requests
from io import StringIO

url = 'https://cdn.buenosaires.gob.ar/datosabiertos/datasets/salud/hospitales/hospitales.geojson'
contenido = StringIO(requests.get(url).text)
objeto = json.load(contenido)
#pprint(objeto)
contenido = requests.get(url).text
objeto = json.loads(contenido)
pprint(objeto)
with open('hospitales_datos.csv','w', newline='',encoding='utf-8') as archivo_out:
    salida = csv.writer(archivo_out)
    salida.writerow(['Nombre','Direccion','Telefono','Especialidad', 'Web'])
    features = objeto['features']
    for feature in features:
        dicc_prop = feature['properties']
        nombre = dicc_prop['NOMBRE']
        direccion = dicc_prop['DOM_NORMA']
        telefono = dicc_prop['TELEFONO']
        especialidad = dicc_prop['TIPO_ESPEC']
        web = dicc_prop['WEB']
        print(nombre, direccion, telefono, especialidad, web)
        salida.writerow([nombre , direccion , telefono , especialidad, web])