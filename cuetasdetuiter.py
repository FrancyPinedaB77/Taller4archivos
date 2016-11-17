from twitter import *
import json
from pymongo import MongoClient
from bson import Binary, Code
#Conexion a MongoDB
cliente = MongoClient()#Inicializar objeto
cliente = MongoClient('127.0.0.1', 27017)#Indicar parametros del servidor
bd = cliente.taller4 #Seleccionar Schema
tweets = bd.tuits_entretenimiento  #Seleccionar Coleccion

#.........................autentificacion...........................
consumer_key= "1vZk3OJcUaiXf1Qe63sRjyCEa"
consumer_secret="hlpnMlZ0ET00KsIluWsDZdHpXrefs6k5DG1sl2jZ5LVl44rnaq"
access_token= "341615632-Hr8Uzc0i9v6e416rRoq5QqlAYLpZrJS9PCqpZbYH"
access_secret="tKz9cnH5E8NDTzWG4MtWrBWGox1wPua71RUDgSFxG1vrl"

twitter = Twitter(auth = OAuth(access_token, access_secret, consumer_key, consumer_secret))


names=["@CineTelevision1","@InfoTVColombia","@Cine_Colombia","@clradiocom","@ModProducciones","@CinePREMIERE","@impactocine","@fotogramas_es","@IMDb","@Fnac_Cine"
,"@Cine_Red","@Univision","@TelemundoLV","@TvsEspectaculos","@canaltnt"]
for recor in names:
	results = twitter.statuses.user_timeline(screen_name =recor, count=200)
	for r in results:
		tweets.insert_one(r)








