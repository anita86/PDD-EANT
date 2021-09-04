# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 19:24:50 2021

@author: Ana
"""
from pprint import pprint

#variable
x = 3
#Lista
lista = []
#Tupla
tupla = ()
#Diccionario
diccionario = {}


edad = 5
le_gusta = ['comer', 'correr a las palomas', 'ladrar de noche']
perro = {'nombre': 'Rocco',
         'tipo' : 'perro',
         'raza' : 'labrador'
         }

#Combinación
perro.update({'edad' : edad})
perro.update({'le_gusta' : le_gusta})

#pprint(perro)
#Nuevo objeto amo
amo = {'nombre' : 'Roberto',
       'tipo' : 'humano',
       'le_gusta': ['Conversar', 'Los animales', 'Partido de fútbol'],
       'edad' : 45,
       'mascota' : perro
       }
pprint(amo)
