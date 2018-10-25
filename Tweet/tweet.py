import tweepy
#tweepy is a module of twitter 

import tokens
#tokens is tokens.py where the token credentials are sotred

consumer_key=tokens.consumer_key()
consumer_secret=tokens.consumer_secret()        #calling the function which was defined in tokens.py
access_key=tokens.access_key()
access_secret=tokens.access_secret()      


auth=tweepy.OAuthHandler(consumer_key,consumer_secret)   #Authentication handler requires consumer key and consumer key secret
auth.set_access_token(access_key,access_secret)          #Access key and Access key secret

user=input("enter the Tweet=")     #user enters of his choice

api=tweepy.API(auth)        #Authentication takes place
api.update_status(user)     #updates the status i.e tweets

