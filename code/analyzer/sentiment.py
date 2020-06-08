# -*- coding: utf-8 -*-

from typing import Text, List

from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier

from variables.envs import logger

class TweetAnalyzer():

  def analyze_sentiment(self, tweet: Text) -> List:
    try:
      analysis = TextBlob(tweet[1])
      if analysis.sentiment.polarity > 0:
        return {
            "code": 1,
            "sentiment": "positivo",
            "tweet_id": tweet[0]}
      elif analysis.sentiment.polarity == 0:
        return {
            "code": 0,
            "sentiment": "neutro",
            "tweet_id": tweet[0]}
      else:
        return {
            "code": -1,
            "sentiment": "negative",
            "tweet_id": tweet[0]}

    except Exception as error:
      logger.error(f"Error tweet analyzer - {error}")

  def get_tweets_sentiment(self, tweets: List, sentiment=None) -> List:
    sentiments = [self.analyze_sentiment(tweet) for tweet in tweets]
    if not sentiment:
      return sentiments
    else:
      if sentiment == "neg":
        return [sentiments[tweet]["code"] for tweet in range(len(sentiments))
          if sentiments[tweet]["code"] < 0]
      elif sentiment == "pos":
        return [sentiments[tweet]["code"] for tweet in range(len(sentiments))
          if sentiments[tweet]["code"] > 0]
      elif sentiment == "neutros":
        return [sentiments[tweet]["code"] for tweet in range(len(sentiments))
          if sentiments[tweet]["code"] == 0]
