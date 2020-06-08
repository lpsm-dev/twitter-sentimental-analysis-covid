# -*- coding: utf-8 -*-

from typing import Text

from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier

class TweetAnalyzer():

  def analyze_sentiment(self, tweet: Text):
    analysis = TextBlob(tweet)

    if analysis.sentiment.polarity > 0:
      return 1, "positivo", tweet
    elif analysis.sentiment.polarity == 0:
      return 0, "neutro", tweet
    else:
      return -1, "negativo", tweet
