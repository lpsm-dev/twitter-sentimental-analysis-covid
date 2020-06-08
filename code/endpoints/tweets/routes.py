# -*- coding: utf-8 -*-

from flask_restplus import Resource

from pprint import pprint

from restplus import api, responses, ns_tweets

from serializers.tweets import tweets_serializer

from actions.twitter import Twitter

from analyzer.sentiment import TweetAnalyzer
from preprocessing.tweet import TweetCleaner

from variables.envs import logger

# ==============================================================================
# GLOBAL
# ==============================================================================

tweet_clean = TweetCleaner(language="english",
  remove_stop_words=False,
  remove_retweets=False
)

query_tweets = {
  "q": "covid-19",
  "result_type": "mixed",
  "count": 100,
  "lang": "en",
}

# ==============================================================================
# ROUTES CORONA
# ==============================================================================

@ns_tweets.route("/corona")
class TweetCoronaNoQuery(Resource):

  @api.doc(description="Route to get corona tweets", responses=responses)
  def get(self):
    logger.info("Getting covid tweets...")
    tweets = tweet_clean.filter_tweets(Twitter().search(**query_tweets))
    try:
      if tweets:
        logger.info("200 - GET - successfully in get corona tweets")
        return {
          "message": responses[200],
          "tweets": tweets
        },  200
      else:
        logger.info("400 - GET - no corona tweets")
        return {
          "message": responses[400],
          "data": []
        },  400
    except Exception as error:
      logger.error("400 - GET - {}".format(error))
      return {
        "message": str(error),
        "data": []
      }, 400

# ==============================================================================
# ROUTES CORONA SENTIMENTAL
# ==============================================================================

@ns_tweets.route("/corona/sentimental")
class TweetCoronaSentimentalNoQuery(Resource):

  @api.doc(description="Route to get corona sentimental tweets", responses=responses)
  def get(self):
    logger.info("Getting sentimental of corona tweets...")
    tweets = [tweet_clean.get_cleaned_text(tweet.text) for tweet in Twitter().search(**query_tweets)]
    try:
      if tweets:
        logger.info("200 - GET - successfully in get corona sentimental tweets")
        analyzer =  TweetAnalyzer()
        sentiments = analyzer.get_tweets_sentiment(tweets, sentiment=None)
        neg = analyzer.get_tweets_sentiment(tweets, sentiment="neg")
        pos = analyzer.get_tweets_sentiment(tweets, sentiment="pos")
        neutros = analyzer.get_tweets_sentiment(tweets, sentiment="neutros")
        return {
          "message": responses[200],
          "data": {
            "sentiments": sentiments,
            "counter": {
              "total": len(sentiments),
              "neg": len(neg),
              "pos": len(pos),
              "neutros": len(neutros)
            },
            "percent": {
              "neg": len(neg)/len(sentiments),
              "pos": len(pos)/len(sentiments),
              "neutros": len(neutros)/len(sentiments),
            }
          }
        },  200
      else:
        logger.info("400 - GET - no corona tweets")
        return {
          "message": responses[400],
          "data": [],
          "count": 0,
        },  400
    except Exception as error:
      logger.error("400 - GET - {}".format(error))
      return {
        "message": str(error),
        "data": [],
        "count": 0,
      }, 400
