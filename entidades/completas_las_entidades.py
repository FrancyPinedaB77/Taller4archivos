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
coleccion = bd.body_pregunta  #Seleccionar Coleccion

st = StanfordNERTagger('/home/xubuntu/Taller4/nueva/classifiers/english.muc.7class.distsim.crf.ser.gz',
	'/home/xubuntu/Taller4/nueva/stanford-ner.jar',encoding='utf-8')

consulta1= coleccion.find({"items.question_id":{"$gte":63724}})
pregunta=0

p=0
y=0
k=0
l=0
m=0
n=0
entidades = []
try:
	bd = cliente.taller4 #Seleccionar Schema
	coleccion = bd.body_respuestas  #Seleccionar Coleccion
	consulta1= coleccion.find({"items.question_id":{"$gte":63724}})
	cliente.close()
	for pregunta in consulta1:
		c= pregunta.get("items")[0]["body"]
		tokenized_text = word_tokenize(c)
		classified_text = st.tag(tokenized_text)
		entidades_personas=[]
		entidades_ubicacion=[]
		entidades_date=[]
		entidades_organization=[]
		entidades_money=[]
		entidades_percent=[]
		entidades=[]
		checker=True
		checked=True
		for z in range (len(classified_text)):		
			if classified_text[z][1]=="PERSON" :
				if classified_text[z+1][1]=="PERSON" :
					entidades_personas.append({p:str(classified_text[z][0]) + " " + str(classified_text[z+1][0])})	
					checker = False
				else:
					if checker:
						entidades_personas.append({p:str(classified_text[z][0])})
					else:
						checker=True
				p=p+1
			elif classified_text[z][1]=="LOCATION":
				if classified_text[z+1][1]=="LOCATION" :
					entidades_ubicacion.append({y:str(classified_text[z][0]) + " " + str(classified_text[z+1][0])})	
					checked= False
				else:
					if checked:
						entidades_ubicacion.append({y:str(classified_text[z][0])})
					else:
						checked=True
				y=y+1
			elif classified_text[z][1]=="DATE":
				entidades_date.append({k:str(classified_text[z][0])})
				k=k+1
			elif classified_text[z][1]=="ORGANIZATION":
				if len(classified_text[z][0])>1:
					entidades_organization.append({l:str(classified_text[z][0])})
					l=l+1	
			elif classified_text[z][1]=="MONEY":
				entidades_money.append({m:str(classified_text[z][0])})
				m=m+1
			elif classified_text[z][1]=="PERCENT":
				entidades_percent.append({n:str(classified_text[z][0])})
				n=n+1
		entidades.append({"PERSON": entidades_personas})
		entidades.append({"LOCATION":entidades_ubicacion})
		entidades.append({"DATE":entidades_date})
		entidades.append({"ORGANIZATION":entidades_organization})
		entidades.append({"MONEY":entidades_money})
		entidades.append({"PERCENT":entidades_percent})#print "el json------------------"
		print json.dumps(entidades)	

except Exception as e:
	print e



#print entidades_ubicacion
#print entidades_date
#print entidades_organization
#print entidades_money
#print entidades_percent