#Contenido del bosdy :{"_id":{"$oid":"58347af4aee0e61156e15b8a"},"has_more":false,"items":[{"body":"\u003cp\u003eThis is \u003ca href=\"http://www.imdb.com/title/tt0113972/\" rel=\"nofollow\"\u003e\u003cem\u003eNick of Time\u003c/em\u003e (1995)\u003c/a\u003e  with Johnny Depp\u003c/p\u003e\n\n\u003cblockquote\u003e\n  \u003cp\u003eAn unimpressive, every-day man is forced into a situation where he is told to kill a politician to save his kidnapped daughter.\u003c/p\u003e\n\u003c/blockquote\u003e\n\n\u003cp\u003e\u003ca href=\"https://en.wikipedia.org/wiki/Nick_of_Time_(film)\" rel=\"nofollow\"\u003eWikipedia\u003c/a\u003e:\u003c/p\u003e\n\n\u003cblockquote\u003e\n  \u003cp\u003eThe film opens with Gene Watson (Johnny Depp), a mild-mannered, widowed accountant arriving with his daughter Lynn at the \u003cstrong\u003eUnion Station in Los Angeles\u003c/strong\u003e [Note not an airport but similar] . As Watson makes a pay phone call informing an unidentified person that his train was late, two mysterious strangers in suits, known only as Mr. Smith (Christopher Walken) and Ms. Jones (Roma Maffia), survey the station from a catwalk, discussing a yet-to-be-elaborated scheme. Noticing Watson retaliate against a skater who was harassing his daughter, \u003cstrong\u003eSmith and Jones set their sights on him\u003c/strong\u003e and swiftly approach the pair. Showing a badge, the two strangers convince Watson that they are police officers and whisk both father and daughter into a van without justification. Once in the vehicle, Watson begins to notice things are not right and gets nervous, but Smith subsequently pistol whips him in the leg to get his attention. Smith then informs Watson that they will kill his daughter by 1:30 p.m. unless he murders a woman depicted in a photograph. He soon learns that the woman is State Governor Eleanor Grant and realizes that killing her would be a suicide mission.\u003c/p\u003e\n\u003c/blockquote\u003e\n","title":"A father is asked to assassinate a political character or his daughter will be shot","tags":["identify-this-movie"],"score":5,"question_id":60001,"answer_id":60002}],"quota_max":10000,"quota_remaining":4999,"entidades":1.0}


from pymongo import MongoClient
import json 
from bson import json_util 
import json

#Conexion a MongoDB
cliente = MongoClient()#Inicializar objeto
cliente = MongoClient('127.0.0.1', 27017)#Indicar parametros del servidor
bd = cliente.taller4 #Seleccionar Schema
coleccion = bd.body_pregunta #Seleccionar Coleccion

pregunta=0
#-----parametros de Consultas en mongo------# respuestas en 63488
consulta1= coleccion.find({"items.question_id":{"$gte":63488}})

for pregunta in consulta1: 			#Llega la consulta
	c= pregunta.get("items")[0]["body"]
	reg = re.compile('([a-zA-Z]{3,}[^0-9])')
    #lista = Counter(ma.group() for ma in reg.finditer(str(arrayList).strip('[]')))
    		

	entidades=json.loads(json.dumps(dict(entidades)))
	coleccion.update({"items.question_id":id_pregunta},{"$set":{"entidades":entidades}},multi=True)        	
