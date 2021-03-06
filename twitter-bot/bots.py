from secrets import *
from bs4 import BeautifulSoup
import requests
import tinyurl
import argparse

# Get commandline arguments
parser = argparse.ArgumentParser()
parser.add_argument("query")
args = parser.parse_args()
print args.query

# Authenticate
auth = tweepy.OAuthHandler(C_KEY, C_SECRET)  
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)  
api = tweepy.API(auth)  

# Query Google
query = args.query 
query = query.replace (" ", "+")
r = requests.get('https://www.google.com.pk/search?q=darjeeling%20sikkim%20assam%20&num=100'.format(query))
soup = BeautifulSoup(r.text, "html.parser")
description = []
links = []

# Parse and clean the results, then tweet!
for item in soup.find_all('h3', attrs={'class' : 'r'}):
    desc = item.text
    #link = tinyurl.create_one(item.a['href'][7:])
    url  = item.a['href'][7:]
    link = url.split("&sa")
    shared_link = tinyurl.create_one(link[0])
    print shared_link
    message = desc +'   '+ shared_link
    tweet = (message[:138] + ' ..') if len(message) > 140 else message
    print "Tweeting the following: "+tweet
    try:
        status = api.update_status(tweet)
    except tweepy.error.TweepError:
        pass

