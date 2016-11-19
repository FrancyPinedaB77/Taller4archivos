import sys
reload(sys)
sys.setdefaultencoding('UTF8')
import json, requests
from pymongo import MongoClient
import stackexchange
import os

#Conexion a MongoDB
cliente = MongoClient()#Inicializar objeto
cliente = MongoClient('127.0.0.1', 27017)#Indicar parametros del servidor
bd = cliente.taller4 #Seleccionar Schema
coleccion = bd.preguntas  #Seleccionar Coleccion

api_key=')F1QD2RiHCaRVYYb5yc3cw(('
site = stackexchange.Site("movies.stackexchange", api_key)
site.include_body=True
site.impose_throttling = True
site.throttle_stop = False
site.answer_tags=True

#Agregados


#DEFINIENDO VARIABLES

page_size=2 #Pagesize can be any value between 0 and 100 and defaults to 30. TRAE ESE NUMERO EN PREGUNTAS 
page_index=9  
from_date=2015-02-01 #  mes y dia 


questions= site.questions(pagesize=page_size, page=page_index, fromdate=from_date, order="asc", sort="creation",title="true", body="true")

print questions


#coleccion.insert_one(questions)


