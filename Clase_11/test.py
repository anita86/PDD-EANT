# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 20:56:50 2021

@author: Ana
"""
#Mi computadora es un servidor web

from flask import Flask, json

app = Flask(__name__)

@app.route("/")
def hello_flask():
    return 'Hola Mundo'

@app.route("/users")
def twitterUsers():
    users = [
        { 'name' : 'smessina_' },
        { 'name' : 'eanteach' },
        { 'name' : 'TinchoLutter' },
        { 'name' : 'bitcoinArg' }
    ]
    response = app.response_class(response = json.dumps(users), status = 200, mimetype = "application/json" )
    
    return response

@app.route("/users/<path>")
def searchUsers(path):

    if path == "people":
        return "Aca va un json de personas" 
    elif path == "company":
        return "Aca va un json de empresas"
    else:
        return "UPS..no puedo buscar lo que estás pidiendo "
    

app.run( port = 3030, host = '0.0.0.0')
