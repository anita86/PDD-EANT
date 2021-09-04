# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 20:18:23 2021

@author: Ana
"""


import csv 
import funciones_norma as fn


with open('reclamos.csv',encoding='ANSI') as archivo_in , open('reclamos_salida.csv','w', encoding='utf-8') as archivo_out:
    entrada = csv.reader(archivo_in)
    salida = csv.writer(archivo_out)
    #archivo_out.write('id_cliente,tx_zona,tx_reclamo,fc_reclamo\n')
    for linea in entrada:
        linea = linea[0].split(';')
        fecha = linea[3]
        try: 
            fecha = fn.normalizadorFechas(fecha,"%d/%m/%Y") 
            print("Metodo 1")
        except:
            try:
                fecha = fn.normalizadorFechas(fecha,"%d-%m-%Y")
                print("Metodo 2")                
            except:
                try: 
                    fecha = fn.normalizadorFechas(fecha,"%Y/%m/%d")
                    print("Metodo 3")
                except:
                    try: 
                        fecha = fn.normalizadorFechas(fecha,"%Y-%d-%m")
                        print("Metodo 4")
                    except:
                        try: 
                            fecha = fn.normalizadorFechas(fecha,"%Y-%m-%d")
                            print("Metodo 5")
                        except:
                            try:
                                fecha = fn.normalizadorFechas(fecha,"%d/%m/%y")
                                print("Metodo 6")
                            except:
                                try: 
                                    fecha = fn.normalizadorFechas(fecha,"%d-%m-%y")
                                    print("Metodo 7")
                                except:
                                    try:
                                        fecha = fn.normalizadorFechas(fn.traductorFecha(fecha),"%d%m%Y")
                                        print("Metodo 8")
                                    except:
                                        print("Error")
        archivo_out.write(fecha + ';' + linea[0] + ';' + linea[1] + ';' + linea[2] + '\n')
                                    
                                    
archivo_in.close()
archivo_out.close()


                                    


