from requests_oauthlib import OAuth1Session
import os


def tweet(twe):
    consumer_key = os.environ['consumer_key']
    consumer_secret = os.environ['consumer_secret']
    base_url = 'https://api.twitter.com/'

    base_json_url = 'https://api.twitter.com/1.1/%s.json'
    tweet = base_json_url % 'statuses/update'
    access_token = {
        'oauth_token': os.environ['oauth_token'],
        'oauth_token_secret': os.environ['oauth_token_secret'],
    }
    twitter = OAuth1Session(
        consumer_key,
        consumer_secret,
        access_token['oauth_token'],
        access_token['oauth_token_secret'],
    )

    response = twitter.post(tweet, params={"status": twe})
