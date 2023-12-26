import spacy
from spacy.lang.pt.examples import sentences

nlp = spacy.load("pt_core_news_sm")
doc = nlp(sentences[0])
print(doc.text)
for token in doc:
    print(token.text, token.pos_, token.dep_)

#script para testar a classificação morfologica das palavras em pt-br - Processamento de linguagem natural