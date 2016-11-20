# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('UTF8')
import json, requests
from pymongo import MongoClient
import urllib2
import json


#Conexion a MongoDB
cliente = MongoClient()#Inicializar objeto
cliente = MongoClient('127.0.0.1', 27017)#Indicar parametros del servidor
bd = cliente.taller4 #Seleccionar Schema
coleccion = bd.body_pregunta  #Seleccionar Coleccion

x=55000 # desde 5 Noviembre
while x <=64000:
    c= "https://api.stackexchange.com/2.1/questions/"+str(x)+"?site=movies.stackexchange&filter=withbody&key=)F1QD2RiHCaRVYYb5yc3cw(("
    x=x+1
    resp = requests.get(url=c)
    data = json.loads(resp.text)
    if (len(data["items"]))!=0:
        #print (data)
        coleccion.insert_one(data)

