# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 19:47:16 2021

@author: Ana
"""

from pymongo import MongoClient

cliente = MongoClient('mongodb://localhost:27017')

estudiante = {'nombre' : 'Ana', 'apellido' : 'Lopez'}

#cliente.universidad.alumnos.insert_one(estudiante)

bd = cliente['universidad']

coleccion = bd['alumnos']

estudiantes = [{'nombre' : 'Diego', 'apellido' : 'Diaz'},
               {'nombre' : 'Julio', 'apellido' : 'Roca', 'dni' : 21555666},
               {'nombre' : 'Alicia', 'apellido' : 'Jimenez', 'hijos' : [{'nombre' : 'Juan', 'edad' : '12'}, {'nombre' : 'Luci', 'edad' : '14'}]}
               ]

coleccion.insert_many(estudiantes)
print("Datos subidos")

