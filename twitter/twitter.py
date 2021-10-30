import tweepy
from twitter import settings


API_KEY = settings.API_KEY
API_SECRET = settings.API_SECRET
ACCESS_TOKEN = settings.ACCESS_TOKEN
ACCESS_SECRET = settings.ACCESS_SECRET


class Tweet(object):
    def __init__(self) -> None:
        self.auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
        self.auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        self.api = tweepy.API(self.auth)

    def post(self, text):
        resp = self.api.update_status(text)
        return resp

    def test_post(self, text):
        print(text)
        return f"This is a mock tweet with {len(text)} characters."
