#ESTE PROGRAMA DEBE TRAER LAS LOCALIZACIONES Y LA INFORMACION DE LA PREGUNTA 
from pymongo import MongoClient
import json 
from bson import json_util 
import json
import sys
import SPARQLWrapper
from SPARQLWrapper import SPARQLWrapper, JSON


#Conexion a MongoDB
cliente = MongoClient()#Inicializar objeto
cliente = MongoClient('127.0.0.1', 27017)#Indicar parametros del servidor
bd = cliente.taller4 #Seleccionar Schema
coleccion = bd.body_pregunta #Seleccionar Coleccion

a=0
pregunta=0
#-----parametros de Consultas en mongo------# respuestas en 63488
consulta1= coleccion.find({"items.question_id":{"$gte":60000}})

for pregunta in consulta1: 			#Llega la consulta
	titulo_pregunta= pregunta.get("items")[0]["title"]
	id_pregunta=int(pregunta.get("items")[0]["question_id"])
	#print texto_marcador
	entidad_localizacion=pregunta.get("entidades")
	a=a+1
	entidad_localizacion=entidad_localizacion.get("LOCATION")
	if entidad_localizacion != None:
		texto_marcador= entidad_localizacion+" "+ "Pregunta #"+str(id_pregunta) + ":" + titulo_pregunta
		print texto_marcador

	#entidades.append(t)
