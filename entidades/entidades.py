from pymongo import MongoClient
import json 
from bson import json_util 
import nltk 
import json
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize

#Conexion a MongoDB
cliente = MongoClient()#Inicializar objeto
cliente = MongoClient('127.0.0.1', 27017)#Indicar parametros del servidor
bd = cliente.taller4 #Seleccionar Schema
coleccion = bd.body_respuestas  #Seleccionar Coleccion

st = StanfordNERTagger('/home/xubuntu/Taller4/nueva/classifiers/english.muc.7class.distsim.crf.ser.gz',
	'/home/xubuntu/Taller4/nueva/stanford-ner.jar',encoding='utf-8')
i=0
pregunta=0
#-----parametros de Consultas en mongo------# respuestas en 63488
consulta1= coleccion.find({"items.question_id":{"$gte":63488}})

for pregunta in consulta1: 			#Llega la consulta
	c= pregunta.get("items")[0]["body"]
	id_pregunta=int(pregunta.get("items")[0]["question_id"])
	print id_pregunta
	tokenized_text = word_tokenize(c) #se separa por palabras
	classified_text = st.tag(tokenized_text) #se usa el clasificador 
	array=classified_text						#aca trae el body de la pregunta separadas las palabras 
	if (len(array))!=0:      
		entidades=[]
		for i in range (len(array)) :
			k=array[i][1]
			if k!="O":
				t=array[i]
				t=list(t)
				t += [t.pop(0)]
				t=tuple(t)
				entidades.append(t)
	entidades=json.loads(json.dumps(dict(entidades)))
	coleccion.update({"items.question_id":id_pregunta},{"$set":{"entidades":entidades}},multi=True)        	
