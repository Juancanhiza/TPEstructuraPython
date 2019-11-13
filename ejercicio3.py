import csv

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
        print(f'- El usuario: {anterior} tiene {apariciones} tweets')
        if apariciones>mayor_apariciones:
            mayor_apariciones = apariciones
            autor_mayor = anterior
        apariciones = 1
    anterior=actual

print(f'+ El usuario que mas tweeteo fue: {autor_mayor} con {mayor_apariciones} tweets')