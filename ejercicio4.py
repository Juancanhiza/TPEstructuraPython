import tweepy
import csv
from tweepy import Stream
from tweepy.streaming import StreamListener
from random import randrange
import json

consumer_key = "S0AENDlf3pPFqqtMMBGrDYB8z"
consumer_secret = "t20hmQFuJ0eb6KmWcAAxaSoh3PmwjLjmii0Ttrzz3oGksSXXxv"
access_key = "1186073449569144832-A3h1HusrVTjjlm29QUCIPXPMqRMN38"
access_secret = "rPLFcHAhxd7cwTdOFuxF3bTNd2Wftw9RvqeUV32Mhiqna"
          
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_key, access_secret) 
api = tweepy.API(auth)

''' PROGRAMA 4 '''

class Listener(StreamListener):
    def on_data(self, tweet):
        try:
            with open('tweets/tweets_tiempo_real.csv', "w") as file:
                print ('Llego un tweet!')
                file.write( tweet + '\n')
                return True
        except BaseException as e:
            print("Error en el dato: %s" % str(e))
        return True

    def on_error(self, estado):
        print(estado)
        return True

tw_stream = Stream(auth, Listener())
tw_stream.filter(track=['#cryptocurrencynews'])