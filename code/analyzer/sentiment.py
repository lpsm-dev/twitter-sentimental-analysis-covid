# -*- coding: utf-8 -*-

from typing import List, Dict
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
from variables.general import logger

class TweetAnalyzer():

  def sentiment_analyze(self, tweet: List) -> Dict:
    try:
      analysis = TextBlob(tweet[1])
      if analysis.sentiment.polarity > 0:
        sentiment = {
          "code": 1,
          "sentiment": "positivo",
          "tweet_id": tweet[0]
        }
      elif analysis.sentiment.polarity == 0:
        sentiment = {
          "code": 0,
          "sentiment": "neutro",
          "tweet_id": tweet[0]
        }
      else:
        sentiment = {
          "code": -1,
          "sentiment": "negative",
          "tweet_id": tweet[0]
        }
    except Exception as error:
      logger.error(f"Error sentiment analyze - {error}")
    else:
      return sentiment

  def get_tweets_sentiment(self, tweets: List, sentiment=None) -> List:
    tweets_sentiment = [self.sentiment_analyze(tweet) for tweet in tweets]
    if not sentiment:
      return tweets_sentiment
    else:
      if sentiment == "neg":
        return [tweets_sentiment[tweet]["code"]
                for tweet in range(len(tweets_sentiment))
                  if tweets_sentiment[tweet]["code"] < 0]
      elif sentiment == "pos":
        return [tweets_sentiment[tweet]["code"]
                for tweet in range(len(tweets_sentiment))
                  if tweets_sentiment[tweet]["code"] > 0]
      elif sentiment == "neutros":
        return [tweets_sentiment[tweet]["code"]
                for tweet in range(len(tweets_sentiment))
                  if tweets_sentiment[tweet]["code"] == 0]
      else:
        logger.error(f"Error invalid sentiment paramater")
