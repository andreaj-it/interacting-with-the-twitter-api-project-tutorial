import os
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()

import tweepy
import requests
import pandas as pandas

consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')
bearer_token = os.environ.get('BEARER_TOKEN')

#print(consumer_key)
# your app code here

client = tweepy.client()

query = ''

tweets = client.search_recent_tweets(query=query, tweet_fields=[])

print(tweets.status_code)

diccionario = tweets.json()
print(type(diccionario))

