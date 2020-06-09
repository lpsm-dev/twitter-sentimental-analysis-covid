# -*- coding: utf-8 -*-

from preprocessing.tweet import TweetCleaner
from analyzer.sentiment import TweetAnalyzer

# ==============================================================================
# GLOBAL
# ==============================================================================

tweet_clean = TweetCleaner(
  language="english",
  remove_stop_words=False,
  remove_retweets=False
)

query_tweets = {
  "q": "covid-19",
  "result_type": "mixed",
  "count": 100,
  "lang": "en",
  "tweet_mode": "extended"
}

analyzer =  TweetAnalyzer()
