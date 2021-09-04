# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 21:18:21 2021

@author: Ana
"""
from datetime import datetime

def normalizadorFechas(fecha, patron_in, patron_out = "%d**%m**%Y"  ):
    objeto_fecha = datetime.strptime(fecha, patron_in)
    fecha_normalizada = datetime.strftime(objeto_fecha,patron_out)
    return fecha_normalizada
    
#fecha a traducir: "13 de enero de 2019"    
def traductorFecha(fecha):
    meses = ['ENERO','FEBRERO','MARZO','ABRIL','MAYO', 'JUNIO', 'JULIO', 'AGOSTO', 'SEPTIEMBRE', 'OCTUBRE', 'NOVIEMBRE', 'DICIEMBRE']
    lista = fecha.split(' ')
    mes = lista[2].upper()
    numero = meses.index(mes) + 1
    fecha_aux = str(lista[0]) + str(numero) + str(lista[4])
    return fecha_aux
