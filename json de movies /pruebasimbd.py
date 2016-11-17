import sys
reload(sys)
sys.setdefaultencoding('UTF8')
import json, requests
from pymongo import MongoClient
#-----------usando imbd-----------------
from imdbpie import Imdb
imdb = Imdb()
imdb = Imdb(anonymize=True)
import re

#Conexion a MongoDB
cliente = MongoClient()#Inicializar objeto
cliente = MongoClient('127.0.0.1', 27017)#Indicar parametros del servidor
bd = cliente.taller4 #Seleccionar Schema
coleccion = bd.peliculas  #Seleccionar Coleccion


movie = str(raw_input('Movie Name: '))
movie_search = '+'.join(movie.split())
    
base_url = 'http://www.imdb.com/find?q='
url = base_url+movie_search+'&s=all'
    
title_search = re.compile('/title/tt\d+')
print base_url



#coleccion.insert_one(top)