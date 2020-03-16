# -*- coding: utf-8 -*-

"""Documentation file clean.py."""

# =============================================================================
# IMPORTS
# =============================================================================

from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier

# =============================================================================
# CLASS - TWEET ANALYZER
# =============================================================================

class TweetAnalyzer():

    def analyze_sentiment(self, tweet):
        analysis = TextBlob(tweet)
        
        if analysis.sentiment.polarity > 0:
            return 1, "positivo", tweet
        elif analysis.sentiment.polarity == 0:
            return 0, "neutro", tweet
        else:
            return -1, "negativo", tweet
