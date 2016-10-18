import tweepy

consumer_key = 'hTM8QyARGUpNS96bBr31tkggf'
consumer_secret = 'UHW3FRTwrNESX57NNLwE4I4s3DDcLpr9aYPphDDEadJcBa7LvS'


def authenticate():
    # create OAuth Handler
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    # get authorisation url
    # TODO : Make the UI better -- colors, bold and stuff
    try:
        auth_url = auth.get_authorization_url(signin_with_twitter=True)
        print("\nPlease go to ", auth_url, " to authorise this app to access your account.\n")
        verifier = input("Enter PIN provided: ")
    except tweepy.TweepError:
        print("Cannot generate authorisation URL")

    # request access token
    try:
        auth.get_access_token(verifier)
        return tweepy.API(auth)
    except tweepy.TweepError:
        print("Failed to acquire access token")