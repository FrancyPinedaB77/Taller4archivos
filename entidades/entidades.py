# -*- coding: utf-8 -*-

import nltk 
import json
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize

st = StanfordNERTagger('/home/xubuntu/Taller4/nueva/classifiers/english.muc.7class.distsim.crf.ser.gz',
					   '/home/xubuntu/Taller4/nueva/stanford-ner.jar',encoding='utf-8')

text = '  loves his country Bogota ,,she will traveled 28 October,  she study in the unversity in Colombia win $8000000 ,she will traveled 28 October, she has $32000'

tokenized_text = word_tokenize(text)
classified_text = st.tag(tokenized_text)
array=classified_text

i=0
entidades=[]
for i in range (len(array)) :
	k=array[i][1]
	if k!="O":
		t=array[i]
		t=list(t)
		t += [t.pop(0)]
		t=tuple(t)
	        entidades.append(t)
entidades=json.dumps(dict(entidades),separators=(',',':'))
print entidades

