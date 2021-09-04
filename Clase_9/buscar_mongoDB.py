# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 21:00:38 2021

@author: Ana
"""

from pymongo import MongoClient

cliente = MongoClient('mongodb://localhost:27017')

bd = cliente['universidad']

coleccion = bd['alumnos']

alumnos = coleccion.find()

# for alumno in alumnos:
#     print(alumno)

estudiante_especial = coleccion.find({'hijos.nombre':'Jimena'})
for e in estudiante_especial:
    print(e)