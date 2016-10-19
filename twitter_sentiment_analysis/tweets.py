import tweepy
import json
from datetime import datetime, timedelta
from twitter_sentiment_analysis import authentication

# TODO: Wrap this in function -- init_api()
api = ''


def init_api():
    """
    Initiliazes the tweepy api object
    """
    global api
    while True:
        try:
            api = authentication.authenticate()
            break
        except tweepy.TweepError as e:
            if '401' in e.reason:
                print("The verification code you entered appears to incorrect.\nWe'll do this once more.")
                # TODO: Check for more error codes


tweets_list = []


def get_tweets_from_previous_weeks(wks=4):
    """
    Retrieves tweets from the the previous number of weeks specified.
    Default = 4 weeks = One last month
    :return: a list of Status objects
    """

    tweet_dates = []
    # load tweets if need be
    if len(tweets_list) == 0:
        load_last_200_tweets()
    else:
        tweet_dates = [datetime.strptime(status['created_at'], '%a %b %d %H:%M:%S %z %Y') for status in tweets_list]
        latest_date = tweets_list[0]
        diff = timedelta(weeks=wks)
        look_for_date = latest_date - diff

        # check if look_for_date is available


def load_last_200_tweets():
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
