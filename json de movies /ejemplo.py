import json, requests
import os 
url = 'https://api.stackexchange.com/2.2/answers?order=desc&sort=activity&site=movies.stackexchange'


resp = requests.get(url=url)
data = json.loads(resp.text)
print data

os.system('mongoimport --db taller4 --collection preguntas <ejemplo.json')