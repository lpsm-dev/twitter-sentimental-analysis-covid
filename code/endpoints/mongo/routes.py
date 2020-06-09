# -*- coding: utf-8 -*-

from flask import jsonify
from flask_restplus import Resource
from restplus import api, responses, ns_mongo
from variables.general import logger
from variables.mongo import mongo

# ==============================================================================
# ROUTES MONGO COVID
# ==============================================================================

@ns_mongo.route("/covid")
class TweetMongoCovidNoQuery(Resource):

  @api.doc(description="Route to get covid tweets from MongoDB", responses=responses)
  def get(self):
    mongo_client = mongo.get_connection()
    db = mongo_client["twitter"]
    collection = db["covid"]
    try:
      logger.info("Getting covid tweets from MongoDB...")
      tweets = [tweet for tweet in collection.find()]
      if len(tweets) == 0:
        logger.warning("No covid tweets. Empty information. Try later.")
    except Exception as error:
      logger.error("400 - GET - {}".format(error))
      return {
        "message": str(error),
        "data": []
      }, 400
    else:
      return jsonify({
        "data": tweets
      })
    mongo.close_connection(mongo_client)

# ==============================================================================
# ROUTES MONGO COVID SENTIMENTAL
# ==============================================================================

@ns_mongo.route("/covid/sentimental")
class TweetMongoCovidSentimentalNoQuery(Resource):

  @api.doc(description="Route to get the sentimental analysis of covid tweets from MongoDB", responses=responses)
  def get(self):
    mongo_client = mongo.get_connection()
    db = mongo_client["twitter"]
    collection = db["sentimental"]
    try:
      logger.info("Getting sentimental analysis of covid tweets from MongoDB...")
      tweets = [{
        "code": tweet["code"],
        "sentiment": tweet["sentiment"],
        "tweet_id": tweet["tweet_id"],
      } for tweet in collection.find()]
      if len(tweets) == 0:
        logger.warning("No covid tweets. Empty information. Try later.")
    except Exception as error:
      logger.error("400 - GET - {}".format(error))
      return {
        "message": str(error),
        "data": []
      }, 400
    else:
      return jsonify({
        "data": tweets
      })
    mongo.close_connection(mongo_client)
