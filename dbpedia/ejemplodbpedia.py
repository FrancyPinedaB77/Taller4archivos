import sys
import SPARQLWrapper
from SPARQLWrapper import SPARQLWrapper, JSON



#TRAE LOS VALORES DE POINT

sparql = SPARQLWrapper("http://dbpedia.org/sparql")

# sparql.setQuery("""
#     PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
#     SELECT ?point
#     WHERE { <http://dbpedia.org/resource/Colombia> georss:point ?point }
# """)
# sparql.setReturnFormat(JSON)
# results = sparql.query().convert()
# print results
# for result in results["results"]["bindings"]:
#     print(result["point"]["value"])

#********************************************************+
#Trae los valores de latitud 

sparql.setQuery("""
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT ?lat
    WHERE { <http://dbpedia.org/resource/India> geo:lat ?lat }
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
for result in results["results"]["bindings"]:
    print len(result)
    lat=(result["lat"]["value"])    
print "esta es la latitut"
print lat
#Trae los valores de longitud 
sparql.setQuery("""
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT ?long
    WHERE { <http://dbpedia.org/resource/India> geo:long ?long }
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
#print results
for result in results["results"]["bindings"]:
    longit=(result["long"]["value"]) 
print "esta es la longitud"   
print longit

