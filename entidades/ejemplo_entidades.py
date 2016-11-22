import ner


tagger = ner.HttpNER(host='127.0.0.1', port=8080)
tagger.get_entities("University of California is located in California, United States")

tagger.json_entities("Alice went to the Museum of Natural History.")
