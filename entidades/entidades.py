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
bd = cliente.ejemploborrar #Seleccionar Schema
coleccion = bd.ejemploborrar  #Seleccionar Coleccion


st = StanfordNERTagger('/home/xubuntu/Taller4/nueva/classifiers/english.muc.7class.distsim.crf.ser.gz',
				   '/home/xubuntu/Taller4/nueva/stanford-ner.jar',encoding='utf-8')

i=0
preguntas=0
#-----parametros de Consultas en mongo------#
consulta1= coleccion.find()

for preguntas in consulta1: 			#Llega la consulta
	'''
	print preguntas.get("items")[0]["body"]
	print  "\n"
        print preguntas.get("items")[0]["question_id"]
	print  "\n"
	'''
	c= preguntas.get("items")[0]["body"]
        id_pregunta=int(preguntas.get("items")[0]["question_id"])
	#print id_pregunta
	c=str(c)			#lo paso a string
	c= c.replace("'"," ")		#le quitan las comillas que generan error
	tokenized_text = word_tokenize(c) #se separa por palabras
	classified_text = st.tag(tokenized_text) #se usa el clasificador 
	array=classified_text						#aca trae el body de la pregunta separadas las palabras 
	#print array
	#---------Haciendo el for para sacar las entidades para cada body 
	#print (len(array))
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
	print entidades
        coleccion.update({"items.question_id":id_pregunta},{"$set":{"entidades":entidades}},multi=True)
        #coleccion.update({},{"$set":{"entidades":entidades}},multi=True)



