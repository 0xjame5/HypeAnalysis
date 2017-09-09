from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import json
import Queue

import pandas as pd
import matplotlib.pyplot as plt


# entering my credentials
access_token = "866498107042926592-mdmmwAFabNev8g8tNKxezUZNt4JEOwC"
access_token_secret = "ydkBqAl5ipTVtqYJufqzz8cSpgjhWGJzc4QCEzUqMsBSl"
consumer_key = "SoVl7EqMxzxiuLqC60pXq5YOn"
consumer_secret = "Rd4SeX53FLHYluxgt6KDVWQJqYBWSfzWFXrLBxpnnfBHY4NU0Z"


testing_queue = Queue.Queue()

json_f = open("file_of_json.txt", 'w')


class StdOutListener(StreamListener):

    def on_data(self, data):
        json_data = json.loads(data)
        json_f.write(data)
        # testing_queue.put(json_data)
        # print json_data

    def on_error(self, status):
        print status

import sys
    
if __name__ == '__main__':
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    print "Getting the tweet________________"
    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'

    try:
        track_tags = ['bitcoin', 'bitcoin price', 'crypto', 'blockchain', 'cryptocurrency', 'BTC', '$BTC', 'crypto market', 
      'bitcoin crash', 'bitcoin china', 'satoshi nakamoto', 'crypto trading']

        stream.filter(track=track_tags, async=True)

    except KeyboardInterrupt:
        sys.exit(1)
