# birdwatch.py
# downloads images on Tweet link provided by user

import tweepy
import json
import argparse
import os, sys

# takes url of tweet and a tweepy twitter api instance as inputs
# returns a list with all media urls or integer -1 if no images on linked tweet
def get_fullres(tweet_url, api_instance):

    pass

# main function, iterates through provided links, downloads any images, and saves them
def main():

    # load secrets from JSON file
    sec_file = './secrets.json' # if you want to use a different file, change this and the .gitignore

    with open(sec_file, 'r') as file:
        secrets = json.load(file)

    # authenticate to twitter API using tweepy
    auth = tweepy.AppAuthHandler(secrets['api_key'], secrets['secret'])

    # get an api object
    api = tweepy.API(auth)
    
    

# run main function
if __name__ == '__main__':
    main()
    