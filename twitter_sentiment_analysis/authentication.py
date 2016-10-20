import tweepy
from twitter_sentiment_analysis.utilities import bcolors

consumer_key = 'hTM8QyARGUpNS96bBr31tkggf'
consumer_secret = 'UHW3FRTwrNESX57NNLwE4I4s3DDcLpr9aYPphDDEadJcBa7LvS'


def authenticate():
    # create OAuth Handler
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    # get authorisation url
    # TODO : Make the UI better -- colors, bold and stuff
    try:
        auth_url = auth.get_authorization_url(signin_with_twitter=True)
        print(bcolors.BOLD, "\nPlease go to",bcolors.ENDC, bcolors.UNDERLINE,  auth_url, bcolors.ENDC,  bcolors.BOLD,
              "\nto authorise this app to access your account.\n", bcolors.ENDC)

        # check that the user inputs a sane input
        while True:
            try:
                verifier = input("Enter PIN provided: ")
                int_value = int(verifier)
                break
            except ValueError:
                print(bcolors.FAIL, verifier, "doesn't seem like a proper verification code. Please check provided code"
                                              " again.\n", bcolors.ENDC)
                continue

    except tweepy.TweepError:
        print ("Cannot generate authorisation URL")

    # request access token
    # Check if access token can obtained. If not raise an Exception.
    # Another request has to be initiated by the init_api function.
    auth.get_access_token(verifier)
    return tweepy.API(auth)
    # try:
    #     auth.get_access_token(verifier)
    #     return tweepy.API(auth)
    # except tweepy.TweepError:
    #     raise
