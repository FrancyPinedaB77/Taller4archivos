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
coleccion = bd.body_respuestas_septiembre  #Seleccionar Coleccion
#DESDE EL NUMERO 600O SE TRAEN CADA 100 Y DESDE 20000 CADA 1000 y desde 63100 cada 10 se retoma en 70000 de 1 en 1
x=60000 #TRAE DATOS DESDE SEPTIEMBRE
while x <=64000:
    c= "https://api.stackexchange.com/2.2/questions/"+str(x)+"/answers?order=desc&sort=activity&site=movies.stackexchange&filter=!2.dt38jGSq_JqOgGGwIVH&impose_throttling%20=True$throttle_stop%20=%20False&key=V4ApLAe)kH*HgBd)*xBXLg(("
    x=x+1
    resp = requests.get(url=c)
    data = json.loads(resp.text)
    if (len(data["items"]))!=0:
        #print (data)
        coleccion.insert_one(data)





#print (data['items'])
#print (len(data['items']))
    #print str(data)
	
    #coleccion.insert_one(data)
