from twitter import *
import json
from pymongo import MongoClient
from bson import Binary, Code
#Conexion a MongoDB
cliente = MongoClient()#Inicializar objeto
cliente = MongoClient('127.0.0.1', 27017)#Indicar parametros del servidor
bd = cliente.grupo14 #Seleccionar Schema
tweets = bd.pertemas  #Seleccionar Coleccion

#.........................autentificacion de la API ...........................
key= ")F1QD2RiHCaRVYYb5yc3cw(("




names=["@JuanManSantos","@AlvaroUribeVel","@petrogustavo","@mluciaramirez","@AABenedetti","@ERobledo","@IvanCepedaCast","@piedadcordoba","@AntanasMockus","@jcvelezuribe","@DanielSamperO","@saludhernandezm","@CristoBustos","@sergio_fajardo","@Timochenko_FARC","@IvanMarquezFARC","@German_Vargas","@ELTIEMPO","@ClaudiaLopez","@RevistaSemana","@VickyDavilaH"]
for recor in names:
	results = twitter.statuses.user_timeline(screen_name =recor, count=100)
	for r in results:
		tweets.insert_one(r)
