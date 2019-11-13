import csv

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
print('Se han ordenado los tweets con exito')