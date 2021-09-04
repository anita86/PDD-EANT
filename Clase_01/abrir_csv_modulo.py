# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 19:26:46 2021

@author: Ana
"""
# import csv 
# #importo metodo csv

# archivo_in = open('peliculas.csv', encoding='utf-8')
# tabla = csv.reader(archivo_in)
# archivo_out = open('peliculas_salida.csv', 'w', encoding='utf-8')

# for linea in tabla:
#     #print(linea)
#     unidos = ','.join([linea[2],linea[1],linea[0]])
#     archivo_out.write(unidos + '\n')
    
    
# archivo_in.close()
# archivo_out.close()

import csv
with open('peliculas.csv', encoding='utf-8') as archivo_in, open('peliculas_salida2.csv', 'w', newline='', encoding='utf-8') as archivo_out:
   entrada = csv.reader(archivo_in)
   salida = csv.writer(archivo_out, delimiter=';')
   salida.writerow(['Director', 'Año', 'Película'])
   for linea in entrada:
      salida.writerow([linea[2], linea[1], linea[0]])