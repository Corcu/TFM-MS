#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      carlos.corcuera.mor1
#
# Created:     23/03/2019
# Copyright:   (c) carlos.corcuera.mor1 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import numpy as np

#librería que se encaga de realizar el analisis de pln
import nltk

#librería para rastrear páginas web
import urllib.request

#import para limpiar la salida de html y evitar las tags
from bs4 import BeautifulSoup

#import para obtener listado de stop words
from nltk.corpus import stopwords

#import para obeter el tokenizador de palabras
from nltk.tokenize import word_tokenize
def main():
    #Buscamos en la página en concreto
    response=urllib.request.urlopen('http://php.net')
    html=response.read()
    #Transformamos la salida para que no tenga tags de html
    soup=BeautifulSoup(html,"html5lib")
    text = soup.get_text(strip=True)
    #tokenizamos el output de la pagina (palabra por palabra)
    tokens=word_tokenize(text)
    #Creamos una copia del listado de tokens para limpiarlo de stop words
    clean_tokens = tokens[:]
    sr = stopwords. words('english')
    #Insertamos signos de puntuacion
    sr.append(',')
    sr.append('.')
    for token in tokens:
        if token in sr:
            clean_tokens.remove(token)
    freq = nltk.FreqDist(clean_tokens)
    for key,val in freq.items():
        print (str(key) + ':' + str(val))
    #Mostramos en un grafico la frecuancia de cada palabra
    freq.plot(20, cumulative=False)
if __name__ == '__main__':
    main()
