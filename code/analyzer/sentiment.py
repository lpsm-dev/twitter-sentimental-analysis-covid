# -*- coding: utf-8 -*-

from typing import Text, List

from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier

from variables.envs import logger

class TweetAnalyzer():

  def analyze_sentiment(self, tweet: Text) -> List:
    try:
      analysis = TextBlob(tweet)
      if analysis.sentiment.polarity > 0:
        return [1, "positivo", tweet]
      elif analysis.sentiment.polarity == 0:
        return [0, "neutro", tweet]
      else:
        return [-1, "negativo", tweet]
    except Exception as error:
      logger.error(f"Error tweet analyzer - {error}")

  def get_tweets_sentiment(self, tweets: List, sentiment=None) -> List:
    sentiments = [self.analyze_sentiment(tweet) for tweet in tweets]
    if not sentiment:
      return sentiments
    else:
      if sentiment == "neg":
        return [sentiments[tweet][0] for tweet in range(len(sentiments))
          if sentiments[tweet][0] < 0]
      elif sentiment == "pos":
        return [sentiments[tweet][0] for tweet in range(len(sentiments))
          if sentiments[tweet][0] > 0]
      elif sentiment == "neutros":
        return [sentiments[tweet][0] for tweet in range(len(sentiments))
          if sentiments[tweet][0] == 0]
