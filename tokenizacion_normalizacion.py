#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      carlos.corcuera.mor1
#
# Created:     30/03/2019
# Copyright:   (c) carlos.corcuera.mor1 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from textblob import TextBlob
import nltk
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import unicodedata
import re
import inflect
import goslate

def main():
    #Insertamos una muestra
    texto_sp = "Hace deporte unas 5 veces a la semana y por la noche a veces estudia."
    #tokenizamos la muestra
    palabras = nltk.word_tokenize(texto_sp)
    print ("tokenizacion")
    print(palabras)
    print("normalizacion")
    palabras = normalize(palabras)
    print(palabras)
    #conversion de lista de tokens en un texto
    resultado = " ".join(palabras)
    analisis=TextBlob(resultado)
    #print("sentimiento")
    #sentimiento = analisis.sentiment
    #print(sentimiento)
    #print("polaridad")
    #popularidad = analisis.polarity
    #print(popularidad)
    print (resultado)

def remove_non_ascii(words):
    """Remove non-ASCII characters from list of tokenized words """
    #Revisar esta funcion porque no filtra nada...
    new_words = []
    for word in words:
        new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        new_words.append(new_word)
    return new_words

def to_lowercase(words):
    """Convert all characters to lowercase from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = word.lower()
        new_words.append(new_word)
    return new_words

def remove_punctuation(words):
    """Remove punctuation from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = re.sub(r'[^\w\s]', '', word)
        if new_word != '':
            new_words.append(new_word)
    return new_words

def replace_numbers(words):
    """Replace all interger occurrences in list of tokenized words with textual representation"""
    p = inflect.engine()
    new_words = []
    for word in words:
        if word.isdigit():
            new_word = p.number_to_words(word)
            new_words.append(new_word)
        else:
            new_words.append(word)
    return new_words

def remove_stopwords(words):
    """Remove stop words from list of tokenized words"""
    new_words = []
    for word in words:
        if word not in stopwords.words('spanish'):
            new_words.append(word)
    return new_words
def stem_words(words):
    """Stem words in list of tokenized words"""
    stemmer = LancasterStemmer()
    stems = []
    for word in words:
        stem = stemmer.stem(word)
        stems.append(stem)
    return stems

def lemmatize_verbs(words):
    """Lemmatize verbs in list of tokenized words"""
    lemmatizer = WordNetLemmatizer()
    lemmas = []
    for word in words:
        lemma = lemmatizer.lemmatize(word, pos='v')
        lemmas.append(lemma)
    return lemmas


def normalize(words):
    words = remove_non_ascii(words)
    words = to_lowercase(words)
    words = remove_punctuation(words)
    words = replace_numbers(words)
    words = remove_stopwords(words)
    return words


if __name__ == '__main__':
    main()
