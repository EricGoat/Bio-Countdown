import tweepy, time, sys
from datetime import datetime

#Grabs Keys for authentication 
keys = open('keys.txt', 'r')
CONSUMER_KEY = keys.readline()
CONSUMER_KEY = CONSUMER_KEY[:-1]
CONSUMER_SECRET = keys.readline()
CONSUMER_SECRET = CONSUMER_SECRET[:-1]
ACCESS_KEY = keys.readline()
ACCESS_KEY = ACCESS_KEY[:-1]
ACCESS_SECRET = keys.readline()

#Authenticate 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#Grabs User Data
user = api.me()
NAME = 'Eric Garcia'
DESCRIPTION = user.description

#Calculates days until birthday 
now = datetime.today()
d0 = datetime(now.year, now.month, now.day)
d1 = datetime(2019, 10, 5)
countdown = d1 - d0
countdown = str(countdown)
countdown = countdown[:-13]

#Updates Description
DESCRIPTION = DESCRIPTION[:-7] + countdown + '🍻 |' 
api.update_profile(NAME, None, None, DESCRIPTION)
