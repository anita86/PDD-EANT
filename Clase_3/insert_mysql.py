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
query = """INSERT INTO alumnos (nombre, apellido, dni, email, fecha_nac)
            VALUES('Angel', 'Nadie', '32333444', 'angel@algo.com', 
            '1999-05-12')"""           
    
cursor.execute(query)
conexion.commit()

cursor.close()
conexion.close()


