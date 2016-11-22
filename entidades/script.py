# -*- coding: utf-8 -*-

import nltk 

from nltk.tag import StanfordNERTagger

from nltk.tokenize import word_tokenize

st = StanfordNERTagger('/home/xubuntu/Taller4/nueva/classifiers/english.muc.7class.distsim.crf.ser.gz',
					   '/home/xubuntu/Taller4/nueva/stanford-ner.jar',encoding='utf-8')

text = 'While in France, Christine Lagarde discussed short-term stimulus efforts in a recent interview with the Wall Street Journal.'

tokenized_text = word_tokenize(text)

classified_text = st.tag(tokenized_text)
#print(classified_text)



array=[(u'While', u'O'), (u'in', u'O'), (u'France', u'LOCATION'), (u',', u'O'), (u'Christine', u'PERSON'), (u'Lagarde', u'PERSON'), (u'discussed', u'O'), (u'short-term', u'O'), (u'stimulus', u'O'), (u'efforts', u'O'), (u'in', u'O'), (u'a', u'O'), (u'recent', u'O'), (u'interview', u'O'), (u'with', u'O'), (u'the', u'O'), (u'Wall', u'O'), (u'Street', u'O'), (u'Journal', u'O'), (u'.', u'O')]
k=array[0][1]
print k

if k=="O":
    print "Funciona "
    

print "textomdmckdsmck"

