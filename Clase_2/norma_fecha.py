# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 20:03:22 2021

@author: Ana
"""

from datetime import datetime

#fecha salida = "13-02-2019"

fecha = '13/02/2019'
objeto_fecha = datetime.strptime(fecha, "%d/%m/%Y")
fecha_normalizada = datetime.strftime(objeto_fecha,"%d-%m-%Y" )
print(fecha, objeto_fecha, fecha_normalizada)