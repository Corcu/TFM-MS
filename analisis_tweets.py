#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Corcu
#
# Created:     27/03/2019
# Copyright:   (c) Corcu 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import tweepy
from time import sleep
from datetime import datetime
from textblob import TextBlob
import matplotlib.pyplot as plt
import datetime

_CONSUMER_KEY           = "GXr9tVc9a82auOZmgAlr6zXBq"
_CONSUMER_SECRET        = "ZtIhAUFvrWlVYTV8vtskEuag9W4SmBCBBsvlVKanP9yXCzkfvO"
_ACCESS_TOKEN           = "143929097-vuEqDC33zpWtkCTxUESChbqiJ5YYqooYhdTOS9Ny"
_ACCESS_TOKEN_SECRET    = "9FohjD8AYwbmwRr7lW3ljWDz9SUT9xMAG3UfhLN5QMkko"
_PERIOD_OF_TIME = 24

def main():
    # Para poder acceder a la API de Twitter he tenido que registrarme como desarrollador, y me han asignado estas 4 claves privadas que se necesitan:

    auth = tweepy.OAuthHandler(_CONSUMER_KEY, _CONSUMER_SECRET)
    api = tweepy.API(auth)
    auth.set_access_token(_ACCESS_TOKEN, _ACCESS_TOKEN_SECRET)

    since = datetime.datetime.now() - datetime.timedelta(hours=_PERIOD_OF_TIME)
    since = str(since.year) + "-" + str(since.month) + "-" + str(since.day)
    palabra = input("Buscar: ")
    numero_de_Tweets = int(input(u"Número de tweets a capturar: "))
    lenguaje = input("Idioma [es/en]:")
    popularidad_list = []
    numeros_list = []
    numero = 1
    for tweet in tweepy.Cursor(api.search, palabra, lang=lenguaje, since = since).items(numero_de_Tweets):
        try:
            #Se toma el texto, se hace el analisis de sentimiento
            #y se agrega el resultado a las listas
            analisis = TextBlob(tweet.text)
            analisis = analisis.sentiment
            popularidad = analisis.polarity
            popularidad_list.append(popularidad)
            numeros_list.append(numero)
            numero = numero + 1

        except tweepy.TweepError as e:
            print(e.reason)

        except StopIteration:
            break
    axes = plt.gca()
    axes.set_ylim([-1, 2])

    plt.scatter(numeros_list, popularidad_list)
    popularidadPromedio = (sum(popularidad_list))/(len(popularidad_list))
    popularidadPromedio = "{0:.0f}%".format(popularidadPromedio * 100)
    #time  = datetime.now().strftime("A : %H:%M\n El: %m-%d-%y")
    plt.text(0, 1.25,
             "Sentimiento promedio:  " + str(popularidadPromedio) + "\n" + since,
             fontsize=12,
             bbox = dict(facecolor='none',
                         edgecolor='black',
                         boxstyle='square, pad = 1'))

    plt.title("Sentimientos sobre " + palabra + " en twitter")
    plt.xlabel("Numero de tweets")
    plt.ylabel("Sentimiento")
    plt.show()






if __name__ == '__main__':
    main()
