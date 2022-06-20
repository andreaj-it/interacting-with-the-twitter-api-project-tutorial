import os
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()

import tweepy
import requests
import pandas as pd
import re

consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')
bearer_token = os.environ.get('BEARER_TOKEN')

#print(consumer_key)
# your app code here

client = tweepy.client(bearer_token=bearer_token,
                        consumer_key=consumer_key,
                        consumer_secret=consumer_secret,
                        access_token=access_token,
                        access_token_secret=access_token_secret,
                        return_type=request.Response,
                        wait_on_rate_limit=True
                        )

#Make a query: Search tweets that have the hashtag #100daysofcode and the word python or pandas, from the last 7 days (search_recent_tweets)
query = '#1000daysofcode(pandas OR python) -is:retweet' #hashtag a buscar

tweets = client.search_recent_tweets(query=query, 
                                tweet_fields=['author_id','created_at','lang'],
                                max_results=100)

#print(tweets.status_code)

tweets_json = tweets.json()

#llevo este json a un diccionario / dataframe
#print(tweets_json)
#print(type(tweets_json))

tweets_data = tweets_json['data'] 

#lo parseamos(normalizamos) y armo el dataframe
df = pd.json_normalize(tweets_data)
#print(df)
#lo guardo
df.to_csv("data/tweets.csv")
