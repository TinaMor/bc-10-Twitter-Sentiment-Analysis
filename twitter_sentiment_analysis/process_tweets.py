import re

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
