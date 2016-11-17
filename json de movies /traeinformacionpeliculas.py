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



url = 'http://www.omdbapi.com/?t=titanic&y=1997'


resp = requests.get(url=url)
data = json.loads(resp.text)
print str(data)
coleccion.insert_one(data)


#infromacion de la api
