# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 20:21:15 2021

@author: Ana
"""
import mysql.connector

conexion = mysql.connector.connect(host = 'cloud.eant.tech',
                                   database = 'pdp_base002',
                                   user = 'pdp_usuario002',
                                   password = 'eantpass')
cursor = conexion.cursor()

#query = "SELECT * FROM alumnos"
query = '''SELECT id, nombre, apellido, dni
            FROM alumnos
            WHERE nombre IN ("Jorge", "Juan", "René", "Carlos")'''
            
    
cursor.execute(query)
for alumno in cursor:
    print(alumno)

cursor.close()
conexion.close()


