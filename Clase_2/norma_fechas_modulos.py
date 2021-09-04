# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 20:18:23 2021

@author: Ana
"""
import funciones_norma as fn
    
fecha = "13/2/2019"
fn.normalizadorFechas(fecha, "%d/%m/%Y")

fecha = "2/13/2019"
fn.normalizadorFechas(fecha, "%m/%d/%Y")

fecha = "02/19" 
fn.normalizadorFechas(fecha, "%m/%y")

fecha = "20191302"
fn.normalizadorFechas(fecha, "%Y%d%m")

fecha = "2019-13-02 14:23:33"
fn.normalizadorFechas(fecha, "%Y-%d-%m %H:%M:%S")

fecha = "13/Feb/2019"
fn.normalizadorFechas(fecha, "%d/%b/%Y")

fecha = "13/February/2019"
fn.normalizadorFechas(fecha, "%d/%B/%Y")

fecha = "13 days after February 2019"
fn.normalizadorFechas(fecha, "%d days after %B %Y")

fecha = "13/Enero/2019"
fn.normalizadorFechas(fn.traductorFecha(fecha), "%d%m%Y")

