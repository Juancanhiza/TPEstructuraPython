import tweepy
import csv
from tweepy import Stream
from tweepy.streaming import StreamListener
from random import randrange

consumer_key = "S0AENDlf3pPFqqtMMBGrDYB8z"
consumer_secret = "t20hmQFuJ0eb6KmWcAAxaSoh3PmwjLjmii0Ttrzz3oGksSXXxv"
access_key = "1186073449569144832-A3h1HusrVTjjlm29QUCIPXPMqRMN38"
access_secret = "rPLFcHAhxd7cwTdOFuxF3bTNd2Wftw9RvqeUV32Mhiqna"
          
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_key, access_secret) 
api = tweepy.API(auth) 

''' PROGRAMA 1 '''
#Se crea el archivo para escritura
file = open("tweets/tweets_billetaje.csv", "w")
file.write('Autor' + ',' + 'Hora' + ',' + 'Fecha' + ',' + 'Texto' + '\n')
search_words = "billetaje electronico"

tweets = tweepy.Cursor(api.search, q=search_words).items(100)
for tweet in tweets:
    creadoenfecha = tweet.created_at
    fecha = str(creadoenfecha.date())
    hora  = str(creadoenfecha.hour) + ":" + str(creadoenfecha.minute)
    autor = tweet.author.screen_name
    texto = str(tweet.text)
    texto = texto.replace('\n', '').replace('\r', '')
    file.write(autor + ',' + hora + ',' + fecha + ',' + texto + '\n')

file.close()
print("Se han obtenido los tweets con exito")