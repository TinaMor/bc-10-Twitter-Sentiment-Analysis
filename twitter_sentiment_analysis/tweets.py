import json
import time
import subprocess
from datetime import datetime, timedelta

import tweepy

import main_utilities
from twitter_sentiment_analysis import authentication
from twitter_sentiment_analysis.utilities import bcolors

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
                print(bcolors.FAIL, "The verification code you entered appears to incorrect."
                                    "\nWe'll do this once more.", bcolors.ENDC)
                # clear screen. Print header only
                time.sleep(2)
                subprocess.call('clear', shell=True)
                print(main_utilities.get_header())
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
        load_latest_200_tweets()
    else:
        tweet_dates = [datetime.strptime(status['created_at'], '%a %b %d %H:%M:%S %z %Y') for status in tweets_list]
        latest_date = tweets_list[0]
        diff = timedelta(weeks=wks)
        look_for_date = latest_date - diff

        # check if look_for_date is available


def load_next_n_tweets(num):
    """
    Loads num tweets to the list of tweets.
    NOTE: The max num allowed is 3200. If num is greater than 3200, num is taken to be 3200
    :param num:
    """
    num = 3200 if num > 3200 else num

    # fetch this directly
    if num < 200:
        for status in tweepy.Cursor(api.user_timeline).items(num):
            tweets_list.append(status._json)
    else:
        iterations, remaining = divmod(num, 200)

        # id of the oldest tweet
        oldest_id = tweets_list[-1]['id'] - 1

        # loop through, add the next 200 tweets
        for i in range(iterations):
            new_tweets = api.user_timeline(count=200, max_id=oldest_id)
            for t in new_tweets:
                tweets_list.append(t._json)
            oldest_id = tweets_list[-1]['id'] - 1

        # add the remaining tweets
        r_tweets = api.user_timeline(count=remaining, max_id=tweets_list[-1]['id'] - 1)
        for i in r_tweets:
            tweets_list.append(i._json)


def load_latest_200_tweets():
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

def get_user_info():
    """
    Returns a dict with user profile information
    :return: a dict with twitter info
    """
    user = api.me()
    return user._json