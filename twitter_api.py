import tweepy
import configparser

#Reads config file

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
access_token = config["twitter"]['access_token']
access_token_secret = config["twitter"]['access_token_secret']

print(api_key)

#authentication 

auth = tweepy.OAuth1UserHandler(api_key,api_key_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

print(public_tweets)

