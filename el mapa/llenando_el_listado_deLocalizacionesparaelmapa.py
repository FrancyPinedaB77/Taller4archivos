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
consulta1= coleccion.find({"items.question_id":{"$gte":63526}})
#------------informacion para traer de DBPEDIA.......................
sparql = SPARQLWrapper("http://dbpedia.org/sparql")


for pregunta in consulta1: 			#Llega la consulta
	titulo_pregunta= pregunta.get("items")[0]["title"]
	id_pregunta=int(pregunta.get("items")[0]["question_id"])
	#print texto_marcador
	entidad_localizacion=pregunta.get("entidades")
	a=a+1
	entidad_localizacion=entidad_localizacion.get("LOCATION")
	if entidad_localizacion != None:
		texto_marcador= entidad_localizacion+" "+ "Pregunta #"+str(id_pregunta) + ":" + titulo_pregunta
		print entidad_localizacion
		lugar= entidad_localizacion
		print lugar
		#se busca la latitud******************* 
		
		#if results
		try :
			sparql.setQuery("""
		    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
		    SELECT ?lat
		    WHERE { <http://dbpedia.org/resource/"""+lugar+"""> geo:lat ?lat }
			""")
			sparql.setReturnFormat(JSON)
			results = sparql.query().convert()
			for trae_latitud in results["results"]["bindings"]:
				print trae_latitud
			punto_latitud=(trae_latitud["lat"]["value"])    
			print "esta es la latitut"
			print punto_latitud
			#se busca la longitud
			sparql.setQuery("""
			    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
			    SELECT ?long
			    WHERE { <http://dbpedia.org/resource/"""+lugar+"""> geo:long ?long }
			""")
			sparql.setReturnFormat(JSON)
			results = sparql.query().convert()
			for trae_longitud in results["results"]["bindings"]:
				a=2
				#print (result["long"]["value"])
			punto_longitud=(trae_longitud["long"]["value"]) 
			print "esta es la longitud"   
			print punto_longitud
		except Exception as error:
			print('ereerror: ' + repr(error)+"-" +lugar +":")


	#entidades.append(t)
