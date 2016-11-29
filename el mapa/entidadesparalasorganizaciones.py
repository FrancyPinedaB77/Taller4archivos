#ESTE PROGRAMA TRAE LA INFORMACION DE  LAS LOCALIZACIONES 

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
trae_todo_coleccion= coleccion.find({"items.question_id":{"$gte":60000}}) #

#------------informacion para traer de DBPEDIA.......................
sparql = SPARQLWrapper("http://dbpedia.org/sparql")
localizaciones_js=[]

for pregunta in trae_todo_coleccion: 			#Llega la consulta
	titulo_pregunta= pregunta.get("items")[0]["title"]
	id_pregunta=int(pregunta.get("items")[0]["question_id"])
	entidad_organizacion=pregunta.get("entidades")
	a=a+1
	entidad_organizacion=entidad_organizacion.get("ORGANIZATION")
	#print entidad_organizacion
	if entidad_organizacion != None:
		entidad_organizacion=entidad_organizacion.title()
		texto_marcador= entidad_organizacion+" "+ "Pregunta #"+str(id_pregunta) + ":" + titulo_pregunta
		lugar= entidad_organizacion
		print lugar
##
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
 					sparql.setQuery("""PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
 					    SELECT ?long
 					    WHERE { <http://dbpedia.org/resource/"""+lugar+"""> geo:long ?long }
 					""")
					sparql.setReturnFormat(JSON)
					results = sparql.query().convert()
					#print results
					for trae_longitud in results["results"]["bindings"]:
						punto_longitud=(trae_longitud["long"]["value"]) 

					array_completo=[str(texto_marcador),float(punto_latitud),float(punto_longitud)]
					print array_completo
					localizaciones_js.append(array_completo)
				print localizaciones_js

		except Exception as error:
			aa=3

print localizaciones_js

