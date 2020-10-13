import tweepy
import time
from Secret.apiKeys import apiKey, apiKeySecret, accessToken, accessTokenSecret

auth = tweepy.OAuthHandler(apiKey, apiKeySecret)

auth.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = "#SaveTheArtsUK"
numberOfTweets = 500

for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        print("Tweet Liked")
        tweet.favorite()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break