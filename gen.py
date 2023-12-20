import markovify
from unidecode import unidecode
import re
import spacy

nlp = spacy.load("en_core_web_sm")

class POSifiedText(markovify.Text):
    def word_split(self, sentence):
        return ["::".join((word.orth_, word.pos_)) for word in nlp(sentence)]

    def word_join(self, words):
        sentence = " ".join(word.split("::")[0] for word in words)
        return sentence

file = open('messages.txt', 'r', encoding=('utf-8'))
texto = file.read()
file.close()

model = markovify.Text(unidecode(str(texto)), state_size=1, well_formed = False)

print(model.make_sentence())