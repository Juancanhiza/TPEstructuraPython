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

# Clase que define los tweets a ser leidos
class Tweet:
    def __init__(self, autor, hora, fecha, texto):
        self.autor = autor
        self.hora = hora
        self.fecha = fecha
        self.texto = texto
    def __getattribute__(self, attr):
        return object.__getattribute__(self, attr)

#Metodos para guardar en una lista los tweets leidos del csv
def autor_menor(tw1, tw2):
    if (tw1.autor < tw2.autor):
        return True
def autor_mayor(tw1, tw2):
    if (tw1.autor >= tw2.autor):
        return True        
def add_tweet(lista_tweets, tw):
    lista_tweets.append(tw)


''' PROGRAMA 5 '''

file = open("tweets/tweets_sorteo.csv", "w")
file.write('Autor' + ',' + 'Hora' + ',' + 'Fecha' + ',' + 'Texto' + '\n')

search_words = "#sorteo"

tweets = tweepy.Cursor(api.search, q=search_words).items(100)
for tweet in tweets:
    creadoenfecha = tweet.created_at
    fecha = str(creadoenfecha.date())
    hora = str(creadoenfecha.hour) + ":" + str(creadoenfecha.minute)
    autor = tweet.author.screen_name
    texto = str(tweet.text)
    texto = texto.replace('\n', '').replace('\r', '')
    file.write(autor + ',' + hora + ',' + fecha + ',' + texto + '\n')

file.close()
print("Se han obtenido los tweets para el sorteo con exito")

tweets_sorteo = []
with open('tweets/tweets_sorteo.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            pass
        add_tweet(tweets_sorteo, Tweet(row["Autor"], row["Hora"], row["Fecha"], row["Texto"]))
        line_count += 1
    #print(f'Se procesaron {line_count} lineas.')

def sorteo (tweets):
    ganador = randrange(100)
    print(f'El numero ganador fue: {ganador}')
    print(f'El ganador del sorteo es: {tweets[ganador].autor}')
    suplente = randrange(100)
    while ganador == suplente:
    	suplente = randrange(100)
    print(f'El numero ganador suplente fue: {suplente}')
    print(f'El ganador suplente del sorteo es: {tweets[suplente].autor}')

sorteo(tweets_sorteo)