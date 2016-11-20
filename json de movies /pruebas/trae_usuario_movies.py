# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('UTF8')
import json, requests
from pymongo import MongoClient



#Conexion a MongoDB
cliente = MongoClient()#Inicializar objeto
cliente = MongoClient('127.0.0.1', 27017)#Indicar parametros del servidor
bd = cliente.taller4 #Seleccionar Schema
coleccion = bd.preguntas  #Seleccionar Coleccion

x=66
while x <=66: #600
    c= "https://api.stackexchange.com//2.2/users/"+str(x)+"?order=desc&sort=reputation&site=movies.stackexchange.com&key=)F1QD2RiHCaRVYYb5yc3cw(("
    #print c
    x=x+1
    resp = requests.get(url=c)
    data = json.loads(resp.text)
    print str(data)
    coleccion.insert_one(data)
