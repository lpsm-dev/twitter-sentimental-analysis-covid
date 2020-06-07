# -*- coding: utf-8 -*-

from tweepy import OAuthHandler, API
from typing import NoReturn, Text, Callable
from tweepy.error import TweepError, RateLimitError

class TwitterBase(object):

    def __init__(self, consumer_key: Text, consumer_secret: Text, access_token: Text, access_token_secret: Text, logger: Callable) -> NoReturn:
        self._consumer_key = consumer_key
        self._consumer_secret =  consumer_secret
        self._access_token = access_token
        self._access_token_secret = access_token_secret
        self._logger = logger

    @property
    def consumer_key(self):
        return self._consumer_key

    @property
    def consumer_secret(self):
        return self._consumer_secret

    @property
    def access_token(self):
        return self._access_token

    @property
    def access_token_secret(self):
        return self._access_token_secret

    @property
    def logger(self) -> Text:
        return self._logger

class TwitterAuthenticator(TwitterBase):

    def __init__(self, consumer_key: Text, consumer_secret: Text, access_token: Text, access_token_secret: Text, logger: Callable):
        super().__init__(consumer_key, consumer_secret, access_token, access_token_secret, logger)

    def authenticate_twitter_app(self):
        auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        return auth

class TwitterClient(TwitterAuthenticator):

    def __init__(self, consumer_key: Text, consumer_secret: Text, access_token: Text, access_token_secret: Text, logger: Callable):
        super().__init__(consumer_key, consumer_secret, access_token, access_token_secret, logger)
        self.auth = self.authenticate_twitter_app()
        self._twitter_client = self.get_twitter_client()

    def get_twitter_client(self) -> Callable:
        twitter_client = API(self.auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        try:
            self.logger.info("Checking Twitter credentials")
            twitter_client.verify_credentials()
        except RateLimitError as error:
            self.logger.error(f"Tweepy RateLimitError - {error}")
        except TweepError as error:
            self.logger.error(f"Tweepy TweepError - {error}")
        except Exception as error:
            self.logger.error(f"Error general exception in   - {error}")
        else:
            self.logger.info("Successful Authentication!")
            return twitter_client

    @property
    def twitter_client(self) -> Text:
        return self._twitter_client
