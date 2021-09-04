# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 21:21:00 2021

@author: Ana
"""

import funciones_norma as fn


fecha = "13 days February 2019"

try: 
    fn.normalizadorFechas(fecha, "%d days after %B %Y")

except:
    print("No funcionó")

