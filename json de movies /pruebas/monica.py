import sys
reload(sys)
sys.setdefaultencoding('UTF8')
import json, requests
from pymongo import MongoClient



#Conexion a MongoDB
cliente = MongoClient()#Inicializar objeto
cliente = MongoClient('127.0.0.1', 27017)#Indicar parametros del servidor
bd = cliente.taller4 #Seleccionar Schema
coleccion = bd.peliculas  #Seleccionar Coleccion




a=["titanic","Die"]
for x in range (len(a)):
	c= 'http://www.omdbapi.com/?t='+a[x]
	print c
	x=x+1
	#print c
	resp = requests.get(url=c)
	data = json.loads(resp.text)
	print str(data)
coleccion.insert_one(data)