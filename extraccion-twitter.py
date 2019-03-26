#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Corcu
#
# Created:     26/03/2019
# Copyright:   (c) Corcu 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import tweepy
import json
import sys
import re
import datetime

# Para poder acceder a la API de Twitter he tenido que registrarme como desarrollador, y me han asignado estas 4 claves privadas que se necesitan:
_CONSUMER_KEY           = "GXr9tVc9a82auOZmgAlr6zXBq"
_CONSUMER_SECRET        = "ZtIhAUFvrWlVYTV8vtskEuag9W4SmBCBBsvlVKanP9yXCzkfvO"
_ACCESS_TOKEN           = "143929097-vuEqDC33zpWtkCTxUESChbqiJ5YYqooYhdTOS9Ny"
_ACCESS_TOKEN_SECRET    = "9FohjD8AYwbmwRr7lW3ljWDz9SUT9xMAG3UfhLN5QMkko"

# Últimas horas en las que buscaremos tuits.
_PERIOD_OF_TIME = 24

# Número de tuits que extraeremos.
_N_ITEMS        = 200

# Esta función la he utilizado para saber todas las propiedades que tiene cada tuit y qué información podemos extraer de cada tuit.
def get_tweet_info(tweet):
    for key, value in tweet._json["user"].items():
        if (value != None):
            try:
                print("Key: " + key + " --> " + str(value))
            except Exception as ex:
                print("Error: " + str(ex))

def get_tweet_info_1(tweet):
    for key, value in tweet._json.items():
        if (value != None):
            try:
                print("Key: " + key + " --> " + str(value))
                for key_2, value_2 in tweet._json[key].items():
                    print("\tKey_2: " + key_2 + " --> " + str(value_2))
            except Exception as ex:
                print("Error: " + str(ex))

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        sys.exit("Error. El programa debe ejecutarse como './tfm.py <hashtag>'")
    else:
        print("Extrayendo todos los tuits que contengan el hashtag '" + str(sys.argv[1]) + "' durante las últimas '" + str(_PERIOD_OF_TIME) + "' horas...")
        try:
            # Autenticación mediante las claves privadas que Twitter facilita a cada desarrollador.
            auth = tweepy.OAuthHandler(_CONSUMER_KEY, _CONSUMER_SECRET)
            auth.set_access_token(_ACCESS_TOKEN, _ACCESS_TOKEN_SECRET)
            api = tweepy.API(auth)
            # En la variable "hashtag" concatenamos la almoadilla con el valor que introduce el usuario mediante la línea de comandos (ej. python tfm.py ms).
            hashtag = "#" + str(sys.argv[1])
            # Calculamos el rango desde el que queremos empezar a buscar tuits. Lo definimos en la variable '_PERIOD_OF_TIME' y se lo restamos a la fecha de hoy.
            since = datetime.datetime.now() - datetime.timedelta(hours=_PERIOD_OF_TIME)
            since = str(since.year) + "-" + str(since.month) + "-" + str(since.day)
            # Creamos un fichero en la misma ubicación donde se encuentra el script tfm.py, y lo llamamos "tuits_<hashtag>.csv".
            f = open("tuits_" + hashtag + ".csv", "w+")
            # Buscamos los tuits que contengan el hashtag introducido, estén escritor en español y hayan sido publicados durante el rango de tiempo que hemos definido. Nos quedamos sólo con el número de tuits definido en la variable 'N_ITEMS'.
            for tweet in tweepy.Cursor(api.search, q = hashtag, lang = "es", since = since).items(_N_ITEMS):
                fecha = re.sub("\t", "", tweet._json["created_at"].encode('utf-8').strip())
                texto = re.sub("\n", "", tweet._json["text"].encode('utf-8').strip())
                user_id = str(tweet._json["user"]["id"])
                retweets = tweet._json["retweet_count"]
                is_verified = tweet._json["user"]["verified"]
                friends = tweet._json["user"]["followers_count"]
                if (tweet._json["geo"] != None):
                    geo_coordinates = str(tweet._json["geo"]["coordinates"])
                else:
                    geo_coordinates = "N/A"
                f.write(user_id + ";" + fecha + ";" + geo_coordinates + ";" + texto + ";" + str(retweets) + ";" + str(is_verified) + ";" + str(friends) + "\n")
                #get_tweet_info_1(tweet)
            f.close()
        except tweepy.error.TweepError as error:
            print(error)