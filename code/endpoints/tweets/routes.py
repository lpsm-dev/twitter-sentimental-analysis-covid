# -*- coding: utf-8 -*-

"""Documentation file routes.py."""

# =============================================================================
# IMPORTS
# =============================================================================

from flask_restplus import Resource
from app.restplus import api, responses, ns_tweets
from app.serializers.tweets import tweets_serializer

from app.settings.log import Log
from app.actions.twitter import Functions
from app.settings.configuration import Configuration

from app.analyzer.clean import TweetCleaner

# =============================================================================
# IMPORTS
# =============================================================================

config = Configuration()

log_path = config.get_env("LOG_PATH") if config.get_env("LOG_PATH") else None
log_file = config.get_env("LOG_FILE") if config.get_env("LOG_FILE") else None

log = Log(log_path, log_file, config.get_env("LOG_LEVEL"), config.get_env("LOGGER")).logger

# =============================================================================
# IMPORTS
# =============================================================================

@ns_tweets.route("/corona")
class TweetCoronaNoQuery(Resource):

    @api.doc(description="Route to get corona tweets", responses=responses)
    def get(self):
        try:
            log.info("Getting corona tweets...")
            tweet_clean = TweetCleaner(remove_stop_words=False, remove_retweets=False)
            query = {"q": "Corona",
                    "result_type": "mixed",
                    "count": 100,
                    "lang": "pt",
                    }
            results = Functions(log).search(**query)

            tweets = [tweet_clean.get_cleaned_text(elemento.text) for elemento in results]
            
            if tweets:
                log.info("200 - GET - successfully in get corona tweets")
                return {"message": responses[200],
                        "data": tweets,
                        "quantidade": len(tweets),
                        "status": 200},  200
            else:
                log.info("400 - GET - no corona tweets")
                return {"message": responses[400],
                        "data": [],
                        "quantidade": 0,
                        "status": 400},  400
        except Exception as error:
            log.error("400 - GET - {}".format(error))
            return {"message": str(error), "data": [], "quantidade": 0, "status": 400}, 400

@ns_tweets.route("")
class TweetNoQuery(Resource):

    @api.expect(tweets_serializer, validate=True)
    @api.doc(description="Route to get tweets", responses=responses)
    def post(self):
        try:
            log.info("Getting tweets...")
            tweet_clean = TweetCleaner(remove_stop_words=False, remove_retweets=False)
            query = api.payload

            results = Functions(log).search(**query)

            tweets = [tweet_clean.get_cleaned_text(elemento.text) for elemento in results]
            
            if tweets:
                log.info("200 - GET - successfully in get tweets")
                return {"message": responses[200],
                        "data": tweets,
                        "quantidade": len(tweets),
                        "status": 200},  200
            else:
                log.info("400 - GET - no tweets")
                return {"message": responses[400],
                        "data": [],
                        "quantidade": 0,
                        "status": 400},  400
        except Exception as error:
            log.error("400 - GET - {}".format(error))
            return {"message": str(error), "data": [], "quantidade": 0, "status": 400}, 400
