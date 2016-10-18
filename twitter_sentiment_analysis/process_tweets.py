import re
from collections import Counter
from twitter_sentiment_analysis import tweets
from watson_developer_cloud import AlchemyLanguageV1
from twitter_sentiment_analysis import utilities

# Thanks to https://marcobonzanini.com/2015/03/09/mining-twitter-data-with-python-part-2/
# Slight modification --- not using emotions for now
regex_str = [
    r'<[^>]+>',  # HTML tags
    r'(?:@[\w]+)',  # @-mentions
    r"(?:\#+[\w]+)",  # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',  # URLs

    r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])",  # words with - and '
    r'(?:[\w_]+)',  # other words
    r'(?:\S)'  # anything else
]

tokens_re = re.compile(r'(' + '|'.join(regex_str) + ')', re.VERBOSE | re.IGNORECASE)


def tokenize(text):
    """
    Tokenizes the text using the rules in pattern tokens_re
    :param text:

    :return: a list of string that make up the text
    """
    return tokens_re.findall(text)


# Count the frequency of words in tweets
def get_word_frequency(tweets_list):
    """
    Counts the frequency of words (appropriate ones)
    :return: a Counter object with word frequency
    """
    tweets_freq_counter = Counter()
    stop_words = utilities.get_stop_words()

    for status in tweets_list:
        tweet_texts = [text for text in tokenize(status['text']) if text not in stop_words]
        tweets_freq_counter.update(tweet_texts)
    return tweets_freq_counter


def get_tweet_texts(tweet_list):
    """
    Builds and returns a single text with the tweets passed
    :param tweet_list:
    :return: a single string with all tweets
    """
    relevant_tweet_text = ''
    for text in tweet_list:
        relevant_tweet_text += ' ' + text['text']

    return relevant_tweet_text


# Initialise the Alchemy API
alchemy_language = AlchemyLanguageV1(api_key="e479d8cc96cefa59286f7871e6b011b734e5131a")


def get_emotion_analysis(text):
    """
    Detects the emotions implied in the text using Alchemy API
    :param text:
    :return: dict of emotions
    """
    return alchemy_language.emotion(text=text)

def get_overall_sentiment(text):
    """
    Detects the
    :param text:
    :return:
    """
