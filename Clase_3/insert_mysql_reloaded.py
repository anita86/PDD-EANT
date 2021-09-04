# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 01:44:14 2021

@author: Ana
"""

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
cursor.execute("SELECT dni FROM alumnos")
lista_dni = [dni[0] for dni in cursor]

continuar = "s"
while continuar == "s":
    dni = input("Ingrese el DNI")    
    if int(dni) in lista_dni:
        print("El DNI ya está registrado")
        continuar = "n"
    else:
        lista_dni.append(int(dni))
        nombre = input("Ingrese el nombre del alumno")
        apellido = input("Ingrese el apellido del alumno")
        email = input("Ingrese el email")
        fecha_nac = input("Ingrese la fecha de nacimiento (Año-mes-día)")
        continuar = input("Desea cargar otro alumno? Seleccione s o n")
        cursor = conexion.cursor()
        query = "INSERT INTO alumnos (nombre, apellido, dni, email, fecha_nac)VALUES(%s,%s,%s,%s,%s)"           
        cursor.execute(query,(nombre, apellido, dni, email, fecha_nac))
        conexion.commit()        


cursor.close()
conexion.close()