
import nltk 
import json
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize

st = StanfordNERTagger('/home/xubuntu/Taller4/nueva/classifiers/english.muc.7class.distsim.crf.ser.gz',
					   '/home/xubuntu/Taller4/nueva/stanford-ner.jar',encoding='utf-8')

text = 'they are Jonny Depp and N. Mandela loves his country Bogota, This are player of soccer James Jennifer,she will traveled 28 October with Michael,  she study in the unversity in Colombia win $8000000 ,she will traveled 28 October,'
tokenized_text = word_tokenize(text)
classified_text = st.tag(tokenized_text)
#print classified_text

array=classified_text
entidades_personas=[]
entidades_ubicacion=[]
p=0
y=0
try:
	for z in range (len(classified_text)):
		if classified_text[z][1]=="PERSON" :
			if classified_text[z+1][1]=="PERSON" :
				entidades_personas.append({z:str(classified_text[z][0]) + " " + str(classified_text[z+1][0])})	
				classified_text.pop(z)
			else:
				entidades_personas.append({z:str(classified_text[z][0])})
		elif classified_text[z][1]=="LOCATION":
			entidades_ubicacion.append({z:str(classified_text[z][0])})

except Exception as e:
	pass
print entidades_personas
print entidades_ubicacion
		
# i=0
# entidades=[]
# for i in range (len(array)) :
# 	k=array[i][1]
# 	if k!="O":
# 		t=array[i]
# 		t=list(t)
# 		t += [t.pop(0)]
# 		t=tuple(t)
# 		entidades.append(t)

		#print entidad1
	    #print entidades
#entidades=json.dumps(dict(entidades))
#print entidades
'''for y in range (len(entidades)):
	#print entidades[y]
	if entidades[y][0]=="PERSON":
		#print entidades[y][1]
		a=2
'''