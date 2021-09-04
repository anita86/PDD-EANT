# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 03:13:28 2021

@author: Ana
"""

from openpyxl import Workbook
from datetime import datetime

wb = Workbook()

#hoja sobre la que vas a trabajar
sheet = wb.active

#completo las celdas
sheet['A1'] = 42

sheet.append([1,'Valor', 341])


sheet['A3'] = datetime.now()


#metodo alternativo: escriboi por coordenadas
sheet.cell(6, 4, 'Alternativo' )

#grabo el archivo
wb.save('ejempli.xlsx')
