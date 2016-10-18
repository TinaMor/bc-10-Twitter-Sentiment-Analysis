import tweepy
import json
from twitter_sentiment_analysis import authentication

# TODO: Wrap this in function -- init_api()
api = ''


def init_api():
    """
    Initiliases the Tweetpy api object
    """
    global api
    api = authentication.authenticate()


tweets_list = []


def get_tweets_from_previous_weeks(weeks=4):
    """
    Retrieves tweets from the the previous number of weeks specified.
    Default = 4 weeks = One last month
    :return:
    """


def get_last_200_tweets():
    """
    Gets the latest 200 tweets if available, add them to tweet_list
    """
    for status in tweepy.Cursor(api.user_timeline).items(200):
        tweets_list.append(status._json)


def save_tweets_json_file():
    """
    Save the collected tweets onto a JSON file
    """
    with open('allTweets.json', 'w') as f:
        json.dump(tweets_list, f)


def load_tweets_json_file():
    """
    Load the JSON file with tweets, decode the data to Python types
    """
    with open('allTweets.json', 'r') as f:
        global tweets_list
        tweets_list = json.load(f)
