# -*- coding: utf-8 -*-
from pymongo import MongoClient
import nltk 
import json
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize


#Conexion a MongoDB
cliente = MongoClient()#Inicializar objeto
cliente = MongoClient('127.0.0.1', 27017)#Indicar parametros del servidor
bd = cliente.taller4 #Seleccionar Schema
coleccion = bd.body_pregunta  #Seleccionar Coleccion


#-----parametros de Consultas en mongo------#

consulta_19= coleccion.find({},{"items.body":1,"_id":0}) 
for user in consulta_19:
	c = user.get("items")
	print c 
print ("debe traer algo ")
