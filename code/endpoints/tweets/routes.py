# -*- coding: utf-8 -*-

from flask_restplus import Resource

from restplus import api, responses, ns_tweets

from serializers.tweets import tweets_serializer

from actions.twitter import Twitter

from tweet.analyzer import TweetAnalyzer
from tweet.cleaner import TweetCleaner

from variables.envs import logger

# ==============================================================================
# ROUTES
# ==============================================================================

@ns_tweets.route("/corona")
class TweetCoronaNoQuery(Resource):

  @api.doc(description="Route to get corona tweets", responses=responses)
  def get(self):
    try:
      logger.info("Getting corona tweets...")

      tweet_clean = TweetCleaner(language="portuguese", remove_stop_words=False, remove_retweets=False)

      query = {
        "q": "#corona",
        "result_type": "mixed",
        "count": 100,
        "lang": "pt",
      }

      results = Twitter().search(**query)

      tweets = [tweet_clean.get_cleaned_text(elemento.text) for elemento in results]

      if tweets:
        logger.info("200 - GET - successfully in get corona tweets")
        return {
          "message": responses[200],
          "data": tweets,
          "quantidade": len(tweets),
          "status": 200
        },  200
      else:
        logger.info("400 - GET - no corona tweets")
        return {
          "message": responses[400],
          "data": [],
          "quantidade": 0,
          "status": 400
        },  400
    except Exception as error:
      logger.error("400 - GET - {}".format(error))
      return {"message": str(error), "data": [], "quantidade": 0, "status": 400}, 400

@ns_tweets.route("/corona/sentimental")
class TweetCoronaSentimentalNoQuery(Resource):

    @api.doc(description="Route to get corona sentimental tweets", responses=responses)
    def get(self):
        try:
            logger.info("Getting corona tweets...")
            tweet_clean = TweetCleaner(remove_stop_words=False, remove_retweets=False)

            query = {"q": "Corona",
                    "result_type": "mixed",
                    "count": 100,
                    "lang": "en",
                    }
            results = Twitter().search(**query)

            tweets = [tweet_clean.get_cleaned_text(elemento.text) for elemento in results]

            if tweets:
                logger.info("200 - GET - successfully in get corona sentimental tweets")

                analyzer = TweetAnalyzer()

                sentiments = [analyzer.analyze_sentiment(elemento) for elemento in tweets]

                negativos = [sentiments[elemento][0] for elemento in range(len(sentiments)) if sentiments[elemento][0] < 0]

                positivos = [sentiments[elemento][0] for elemento in range(len(sentiments)) if sentiments[elemento][0] > 0]

                neutros = [sentiments[elemento][0] for elemento in range(len(sentiments)) if sentiments[elemento][0] == 0]

                return {"message": responses[200],
                        "data": sentiments,
                        "quantidade": len(sentiments),
                        "negativos": len(negativos),
                        "positivos": len(positivos),
                        "neutros": len(neutros),
                        "porcentagem_negativos": len(negativos)/len(sentiments),
                        "porcentagem_positivos": len(positivos)/len(sentiments),
                        "porcentagem_neutros": len(neutros)/len(sentiments),
                        "status": 200},  200
            else:
                logger.info("400 - GET - no corona tweets")
                return {"message": responses[400],
                        "data": [],
                        "quantidade": 0,
                        "status": 400},  400
        except Exception as error:
            logger.error("400 - GET - {}".format(error))
            return {"message": str(error), "data": [], "quantidade": 0, "status": 400}, 400

@ns_tweets.route("")
class TweetNoQuery(Resource):

    @api.expect(tweets_serializer, validate=True)
    @api.doc(description="Route to get tweets", responses=responses)
    def post(self):
        try:
            logger.info("Getting tweets...")
            tweet_clean = TweetCleaner(remove_stop_words=False, remove_retweets=False)
            query = api.payload

            results = Twitter().search(**query)

            tweets = [tweet_clean.get_cleaned_text(elemento.text) for elemento in results]

            if tweets:
                logger.info("200 - GET - successfully in get tweets")
                return {"message": responses[200],
                        "data": tweets,
                        "quantidade": len(tweets),
                        "status": 200},  200
            else:
                logger.info("400 - GET - no tweets")
                return {"message": responses[400],
                        "data": [],
                        "quantidade": 0,
                        "status": 400},  400
        except Exception as error:
            logger.error("400 - GET - {}".format(error))
            return {"message": str(error), "data": [], "quantidade": 0, "status": 400}, 400

@ns_tweets.route("/sentimental")
class TweetSentimentalNoQuery(Resource):

    @api.expect(tweets_serializer, validate=True)
    @api.doc(description="Route to get tweets", responses=responses)
    def post(self):
        try:
            logger.info("Getting tweets...")
            tweet_clean = TweetCleaner(remove_stop_words=False, remove_retweets=False)
            query = api.payload

            results = Twitter().search(**query)

            tweets = [tweet_clean.get_cleaned_text(elemento.text) for elemento in results]

            if tweets:
                logger.info("200 - GET - successfully in get sentimental tweets")

                analyzer = TweetAnalyzer()

                sentiments = [analyzer.analyze_sentiment(elemento) for elemento in tweets]

                negativos = [sentiments[elemento][0] for elemento in range(len(sentiments)) if sentiments[elemento][0] < 0]

                positivos = [sentiments[elemento][0] for elemento in range(len(sentiments)) if sentiments[elemento][0] > 0]

                neutros = [sentiments[elemento][0] for elemento in range(len(sentiments)) if sentiments[elemento][0] == 0]

                return {"message": responses[200],
                        "data": sentiments,
                        "quantidade": len(sentiments),
                        "negativos": len(negativos),
                        "positivos": len(positivos),
                        "neutros": len(neutros),
                        "porcentagem_negativos": len(negativos)/len(sentiments),
                        "porcentagem_positivos": len(positivos)/len(sentiments),
                        "porcentagem_neutros": len(neutros)/len(sentiments),
                        "status": 200},  200
            else:
                logger.info("400 - GET - no tweets")
                return {"message": responses[400],
                        "data": [],
                        "quantidade": 0,
                        "status": 400},  400
        except Exception as error:
            logger.error("400 - GET - {}".format(error))
            return {"message": str(error), "data": [], "quantidade": 0, "status": 400}, 400
