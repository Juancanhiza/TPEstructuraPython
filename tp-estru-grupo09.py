import tweepy 
import csv
from tweepy import Stream
from tweepy.streaming import StreamListener
from random import randrange

consumer_key = "CONSUMER_KEY"
consumer_secret = "CONSUMER_SECRET"
access_key = "ACCESS_KEY"
access_secret = "ACCESS_SECRET"
          
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
    hora = str(creadoenfecha.hour) + ":" + str(creadoenfecha.minute)
    autor = tweet.author.screen_name
    texto = str(tweet.text)
    texto = texto.replace('\n', '').replace('\r', '')
    file.write(autor + ',' + hora + ',' + fecha + ',' + texto + '\n')

file.close()
print("Se han obtenido los tweets con exito")

''' PROGRAMA 2 '''

def quicksort_tw(lista):
    if not lista:
        return []
    else:
        pivote = lista[-1]
        menor = [x for x in lista if autor_menor(x, pivote)]
        mas_grande = [ x for x in lista[:-1] if autor_mayor(x, pivote)]
        return quicksort_tw(menor) + [pivote] + quicksort_tw(mas_grande)

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


# SE LEEN LOS TWEETS Y SE GUARDAN EN UNA LISTA

lista_de_tweets = []
with open('tweets/tweets_billetaje.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            pass
        add_tweet(lista_de_tweets, Tweet(row["Autor"], row["Hora"], row["Fecha"], row["Texto"]))
        line_count += 1
    #print(f'Se procesaron {line_count} lineas.')

tweets_ordenados = quicksort_tw(lista_de_tweets)
#print(f'cantidad de tweets ordenados = {len(tweets_ordenados)}')
file_ordenados = open("tweets/tweets_billetaje_ordenados.csv", "w")
file_ordenados.write('Autor' + ',' + 'Hora' + ',' + 'Fecha' + ',' + 'Texto' + '\n')

for tweet in tweets_ordenados:
    autor = str(tweet.autor)
    hora = str(tweet.hora)
    fecha = str(tweet.fecha)
    texto = str(tweet.texto)
    file_ordenados.write(autor + ',' + hora + ',' + fecha + ',' + texto + '\n')

file_ordenados.close()


''' PROGRAMA 3 '''
# Se leen los tweets y se realiza el conteo

tweets = []
with open('tweets/tweets_billetaje_ordenados.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            pass
        add_tweet(tweets, Tweet(row["Autor"], row["Hora"], row["Fecha"], row["Texto"]))
        line_count += 1
    #print(f'Se procesaron {line_count} lineas.')

mayor_apariciones = 0
apariciones = 0
anterior = tweets[0].autor

for tw in tweets:
    actual = tw.autor
    if anterior == actual:
        apariciones += 1
    else:
        if apariciones>mayor_apariciones:
            mayor_apariciones = apariciones
            autor_mayor = anterior
        apariciones = 1
    anterior=actual

print(f'El usuario que más tweeteo fue:{autor_mayor} con {mayor_apariciones} tweets')



''' PROGRAMA 4 '''
'''
class Listener(StreamListener):
    def on_data(self, tweet):
        try:
            with open('tweets/tweets_tiempo_real.csv', "w") as file:
                print ('Llegó un tweet!')
                file.write( tweet + '\n')
                return True
        except BaseException as e:
            print("Error en el dato: %s" % str(e))
        return True

    def on_error(self, estado):
        print(estado)
        return True

tw_stream = Stream(auth, Listener())
tw_stream.filter(track=['#python'])
'''

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

sorteo(tweets_sorteo)

