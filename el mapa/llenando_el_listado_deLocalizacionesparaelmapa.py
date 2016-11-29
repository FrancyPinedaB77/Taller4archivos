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
coleccion = bd.preguntasdesdejunio #Seleccionar Coleccion

a=0
pregunta=0
#-----parametros de Consultas en mongo------# respuestas en 63488
consulta1= coleccion.find({"items.question_id":{"$gte":55059}}) #
#------------informacion para traer de DBPEDIA.......................
sparql = SPARQLWrapper("http://dbpedia.org/sparql")
localizaciones_js=[]

for pregunta in consulta1: 			#Llega la consulta
	titulo_pregunta= pregunta.get("items")[0]["title"]
	id_pregunta=int(pregunta.get("items")[0]["question_id"])
	#print texto_marcador
	entidad_localizacion=pregunta.get("entidades")
	a=a+1
	entidad_localizacion=entidad_localizacion.get("LOCATION")
	if entidad_localizacion != None:
		entidad_localizacion=entidad_localizacion.title()
		texto_marcador= entidad_localizacion+" "+ "Pregunta #"+str(id_pregunta) + ":" + titulo_pregunta
		lugar= entidad_localizacion
		#print lugar
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
			for prueba_que_tenga in results["results"]["bindings"]:
				if len(prueba_que_tenga)==1:
					for trae_latitud in results["results"]["bindings"]:
						punto_latitud=(trae_latitud["lat"]["value"]) 
					#print texto_marcador   
					#print "esta es la latitut" +"de" + lugar
					#print punto_latitud
					#se busca la longitud
					sparql.setQuery("""
					    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
					    SELECT ?long
					    WHERE { <http://dbpedia.org/resource/"""+lugar+"""> geo:long ?long }
					""")
					sparql.setReturnFormat(JSON)
					results = sparql.query().convert()
					for trae_longitud in results["results"]["bindings"]:
						punto_longitud=(trae_longitud["long"]["value"]) 
					#print "esta es la longitud" +"de" + lugar
					#print punto_longitud
					#print "-------------------------------------------------------------"
					array_completo=[str(texto_marcador),float(punto_latitud),float(punto_longitud)]
					#print array_completo
					localizaciones_js.append(array_completo)
				print localizaciones_js

		except Exception as error:
			aa=3
			#print('ereerror: ' + repr(error)+"-" +lugar +":")
print localizaciones_js
	#entidades.append(t)
