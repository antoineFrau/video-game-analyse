from textblob import TextBlob
import tweepy
import numpy as np
import json
from pytrends.request import TrendReq
import datetime
import time

consumer_key = "YOUR_KEY_HERE"
consumer_secret = "YOUR_KEY_HERE"
access_token = "YOUR_KEY_HERE"
access_token_secret = "YOUR_KEY_HERE"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

pytrend = TrendReq()

def handle_json_load(filename):
    with open(filename) as handle:
        return json.loads(handle.read())

def handle_json_dump(filename, json_string):
    with open(filename, 'w') as handle:
        _ = json.dump(json_string, handle)
        

def get_sentiments_from_object(tweets):
    positif = negatif = neutral = 0

    for status in tweets:
        testimonial = TextBlob(status.full_text)
        if testimonial.sentiment.polarity < 0:
            negatif += 1
        elif testimonial.sentiment.polarity > 0:
            positif += 1
        else:
            neutral += 1
    return [negatif, positif, neutral]


def get_trends(keyword, key, start_at, end_at):
    timeframe = start_at + ' ' + end_at 

    # setyp Google Trend API request
    pytrend.build_payload(kw_list=[keyword], timeframe=timeframe)

    result = {
        "cities": {},
        "evolutions": {}
    }

    # Interest Over Time
    interest_over_time_df = pytrend.interest_over_time()
    evolutions = interest_over_time_df.to_dict()[keyword]
    for i in evolutions:
        d = i.strftime("%Y-%m-%d")
        result['evolutions'][d] = evolutions[i]
    
    # Interest Over Time
    interest_by_region_df = pytrend.interest_by_region(resolution='COUNTRY')
    interest_by_region_df = interest_by_region_df[interest_by_region_df[keyword] != 0]
    result['cities'] = interest_by_region_df.to_dict()[keyword]
    return result


def get_stats(keyword, key, n):
    tweets = []
    for item in tweepy.Cursor(api.search, lang='en', q=keyword, tweet_mode='extended').items(n):
        tweets.append(item)
    
    filename = key+'.json'
    handle_json_dump(filename, [item._json for item in tweets])

    result_research[key]["nb_tweets"] = n
    
    count_sentiment = get_sentiments_from_object(tweets)
    
    pernegatif = ((count_sentiment[0] / float(n)) * 100.0)
    perpositif = ((count_sentiment[1] / float(n)) * 100.0)
    perneutral = ((count_sentiment[2] / float(n)) * 100.0)
    
    result_research[key]["sentiment"] = [pernegatif, perpositif, perneutral]
    s_at = result_research[key]["trends"]["start_at"]
    e_at = result_research[key]["trends"]["end_at"]
    
    trends = get_trends(keyword, key, s_at, e_at)
    result_research[key]["trends"]["cities"] = trends["cities"]
    result_research[key]["trends"]["evolutions"] = trends["evolutions"]


result_research = handle_json_load('result.json')
number = 500
keys = ["red_dead_redemption_2", "monster_hunter_world", "fallout_76", "marvel_spider_man", "god_of_war"]
for i in range(len(keys)):
    
    item = result_research[keys[i]]

    get_stats(item['keyword'], keys[i], number)
    save_json = handle_json_dump('result.json', result_research)
    # Wait 2 minutes until requesting again Twitter API.
    # Avoid me to never get banned
    time.sleep(120)