# -*- coding: utf-8 -*-

from flask import jsonify
from flask_restplus import Resource
from pymongo.errors import DuplicateKeyError
from restplus import api, responses, ns_tweets
from actions.twitter import Twitter
from variables.general import logger
from variables.mongo import mongo
from variables.tweet import tweet_clean, query_tweets, analyzer

# ==============================================================================
# ROUTES COVID
# ==============================================================================

@ns_tweets.route("/covid")
class TweetCovidNoQuery(Resource):

  @api.doc(description="Route to get covid tweets", responses=responses)
  def get(self):
    logger.info("GET - covid tweets...")
    tweets = tweet_clean.filter_tweets(Twitter().search(**query_tweets))
    mongo_client = mongo.get_connection()
    db = mongo_client["twitter"]
    collection = db["covid"]
    if tweets:
      logger.info("200 - GET - successfully get covid tweets")
      for tweet in tweets:
        try:
          found = collection.find({
            "_id": dict(tweet)["_id"]
          }).limit(1).count()
          if found > 0:
            logger.info("Data alredy exist in MongoDB. Continue...")
            continue
          else:
            insert = collection.insert_one(tweet)
            if insert.inserted_id:
              logger.info("Insert data covid tweet in MongoDB - Successfully insert data!")
            else:
              logger.error("Insert data covid tweet in MongoDB - Bad insert data...")
        except DuplicateKeyError as error:
          logger.error("400 - GET - no covid tweets")
          logger.error(f"DuplicateKeyError - {error}")
          return {
            "message": responses[400],
            "count": 0
          },  400
      return {
        "message": responses[200],
        "count": len(tweets)
      },  200
    else:
      logger.error("400 - GET - no covid tweets")
      return {
        "message": responses[400],
        "count": 0
      },  400
    mongo.close_connection(mongo_client)

# ==============================================================================
# ROUTES COVID SENTIMENTAL
# ==============================================================================

@ns_tweets.route("/covid/sentimental")
class TweetCovidSentimentalNoQuery(Resource):

  @api.doc(description="Route to get the sentimental analysis of covid tweets", responses=responses)
  def get(self):
    logger.info("GET - sentimental analysis of covid tweets...")
    mongo_client = mongo.get_connection()
    db = mongo_client["twitter"]
    collection_covid = db["covid"]
    collection_sentimental = db["sentimental"]
    if collection_sentimental.count() == 0:
      logger.info("Sentimental collection is empty")
      if "sentimental" in db.list_collection_names():
        logger.info("Sentimental collection exist")
      else:
        logger.info("Sentimental collection not exist")
    else:
      logger.info("Sentimental collection is not empty")
    try:
      tweets = [
        [
          tweet["_id"],
          tweet["full_text"]
        ] for tweet in [tweet for tweet in collection_covid.find()]
      ]
      if len(tweets) == 0:
        logger.warning("No covid tweets. Empty information")
    except Exception as error:
      logger.error("400 - GET - {}".format(error))
      return {
        "message": str(error),
        "count": 0
      }, 400
    if tweets:
      sentiments = analyzer.get_tweets_sentiment(tweets, sentiment=None)
      if sentiments:
        logger.info("200 - GET - successfully get sentimental analysis of covid tweets")
        neg = analyzer.get_tweets_sentiment(tweets, sentiment="neg")
        pos = analyzer.get_tweets_sentiment(tweets, sentiment="pos")
        neutros = analyzer.get_tweets_sentiment(tweets, sentiment="neutros")
        for tweet in sentiments:
          try:
            found = collection_sentimental.find({
              "tweet_id": dict(tweet)["tweet_id"]
            }).limit(1).count()
            if found > 0:
              logger.info("Data alredy exist in MongoDB. Continue...")
              continue
            else:
              insert = collection_sentimental.insert_one(tweet)
              if insert.inserted_id:
                logger.info("Insert data sentimental analysis in MongoDB - Successfully insert data!")
              else:
                logger.error("Insert data sentimental analysis in MongoDB - Bad insert data...")
          except pymongo.errors.DuplicateKeyError as error:
            logger.error("400 - GET - no data sentimental analysis of covid tweets")
            logger.error(f"DuplicateKeyError - {error}")
            return {
              "message": responses[400],
              "count": 0
            },  400
        return {
          "message": responses[200],
          "count": len(sentiments)
        },  200
      else:
        logger.error("400 - GET - no data sentimental analysis of covid tweets")
        return {
          "message": responses[400],
          "count": 0,
        },  400
    else:
      logger.info("400 - GET - no covid tweets")
      return {
        "message": responses[400],
        "data": [],
        "count": 0,
      },  400
    mongo.close_connection(mongo_client)
