import unittest
from twitter_sentiment_analysis import authentication
class AuthenticationTests(unittest.TestCase):
    """
    Tests the authentication with Twitter
    """
    def test_generates_auth_url(self):
        """
        Should be able to generate an authentication URL to enable user authorise the app
        """
        self.assertEqual(True, authentication.authenticate() != None)