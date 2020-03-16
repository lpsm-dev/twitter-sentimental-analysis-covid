# -*- coding: utf-8 -*-

"""Documentation file clean.py."""

# =============================================================================
# IMPORTS
# =============================================================================

import re
import emoji

from nltk.corpus import stopwords

# =============================================================================
# CLASS - TWEET CLEANER
# =============================================================================

class TweetCleaner(object):

    def __init__(self, remove_stop_words=False, remove_retweets=False):
        if remove_stop_words:
            self.stop_words = set(stopwords.words("portuguese"))
        else:
            self.stop_words = set()
        self.remove_retweets = remove_retweets

    def give_emoji_free_text(self, text):
        allchars = [str for str in text]
        emoji_list = [c for c in allchars if c in emoji.UNICODE_EMOJI]
        clean_text = " ".join([str for str in text.split() if not any(i in str for i in emoji_list)])
        return clean_text
      
    def get_cleaned_text(self, text):
        cleaned_text = text.replace("\n", "").replace('\"','').replace('\'','').replace('-',' ')

        if re.match(r"RT @[_A-Za-z0-9]+:", cleaned_text): # retweet
            if self.remove_retweets: return ""
            retweet_info = cleaned_text[:cleaned_text.index(':')+2] # 'RT @name: ' will be again added in the text after cleaning
            cleaned_text = cleaned_text[cleaned_text.index(':')+2:]
        else:
            retweet_info = ""

        cleaned_text = re.sub(r"@[a-zA-Z0-9_]+", "", (retweet_info + cleaned_text)).strip()
        cleaned_text = re.sub(r"RT\s:\s", "", cleaned_text).lstrip()
        cleaned_text = cleaned_text[::] if cleaned_text[0] != " " else cleaned_text[1::]
        cleaned_text = self.give_emoji_free_text(cleaned_text)
        cleaned_text = re.sub(r"http\S+", "", cleaned_text)
        cleaned_text = re.sub(r"https\S+", "", cleaned_text)

        return cleaned_text
