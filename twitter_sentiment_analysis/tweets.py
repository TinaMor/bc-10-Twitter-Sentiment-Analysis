import tweepy
from twitter_sentiment_analysis import authentication

api = authentication.authenticate()

tweets_list = []


def get_last_200_tweets():
    """
    Gets the latest 200 tweets if available, add them to tweet_list
    """
    for status in tweepy.Cursor(api.user_timeline).items(200):
        tweets_list.append(status)
