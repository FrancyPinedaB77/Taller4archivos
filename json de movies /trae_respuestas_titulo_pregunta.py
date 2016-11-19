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
coleccion = bd.preguntas2  #Seleccionar Coleccion

x=905
while x <=905:
    c= "https://api.stackexchange.com/2.2/questions/"+str(x)+"/answers?order=desc&sort=activity&site=movies.stackexchange&filter=!2.dt38jGSq_JqOgGGwIVH"
    x=x+1
    resp = requests.get(url=c)
    data = json.loads(resp.text)
    if (len(data["items"]))!=0:
        #data = json.dumps(data.text, ensure_ascii=False).encode('utf8')
        print (data)
        coleccion.insert_one(data)

#print (data['items'])
#print (len(data['items']))
    #print str(data)
	
    #coleccion.insert_one(data)
