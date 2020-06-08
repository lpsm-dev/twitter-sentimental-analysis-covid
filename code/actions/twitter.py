# -*- coding: utf-8 -*-

from typing import NoReturn, List
from clients.twitter import TwitterClient
from variables.envs import (twitter_consumer_key,
                            twitter_consumer_secret,
                            twitter_access_token,
                            twitter_access_token_secret,
                            logger)

class Twitter(object):

  def __init__(self) -> NoReturn:
    self.twitter = TwitterClient(
      twitter_consumer_key,
      twitter_consumer_secret,
      twitter_access_token,
      twitter_access_token_secret
    ).twitter_client

  def search(self, **query) -> List:
    try:
      search = [elemento for elemento in self.twitter.search(**query) if elemento]
    except Exceptio as error:
      logger.error(f"Error twitter client search - {Exceptio}")
    else:
      return search
