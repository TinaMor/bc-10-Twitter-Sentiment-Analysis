import tweepy

consumer_key = 'hTM8QyARGUpNS96bBr31tkggf'
consumer_secret = 'UHW3FRTwrNESX57NNLwE4I4s3DDcLpr9aYPphDDEadJcBa7LvS'

def authenticate():
    # create OAuth Handler
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    # get authorisation url
    try:
        auth_url = auth.get_authorization_url(signin_with_twitter=True)
        print(auth_url)
    except tweepy.TweepError:
        print("Cannot get request token")
