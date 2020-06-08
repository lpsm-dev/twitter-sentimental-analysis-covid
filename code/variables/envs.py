# -*- coding: utf-8 -*-

from tools.os import OS
from settings.log import Log
from settings.config import Config

from database.mongo import Mongo

# ==============================================================================
# GLOBAL
# ==============================================================================

config = Config()

twitter_consumer_key = config.get_env("TWITTER_CONSUMER_KEY") if config.get_env("TWITTER_CONSUMER_KEY") else None
twitter_consumer_secret = config.get_env("TWITTER_CONSUMER_SECRET") if config.get_env("TWITTER_CONSUMER_SECRET") else None
twitter_access_token = config.get_env("TWITTER_ACCESS_TOKEN") if config.get_env("TWITTER_ACCESS_TOKEN") else None
twitter_access_token_secret = config.get_env("TWITTER_ACCESS_TOKEN_SECRET") if config.get_env("TWITTER_ACCESS_TOKEN_SECRET") else None

log_path = config.get_env("LOG_PATH") if config.get_env("LOG_PATH") else "/var/log/code"
log_file = config.get_env("LOG_FILE") if config.get_env("LOG_FILE") else "file.log"
log_level = config.get_env("LOG_LEVEL") if config.get_env("LOG_LEVEL") else "DEBUG"
logger_name = config.get_env("LOGGER_NAME") if config.get_env("LOGGER_NAME") else "Sentiment Analysis"

logger = Log(log_path, log_file, log_level, logger_name).logger

mongo_host = config.get_env("MONGO_HOST") if config.get_env("MONGO_HOST") else "mongodb"
mongo_user = config.get_env("MONGO_INITDB_ROOT_USERNAME") if config.get_env("MONGO_INITDB_ROOT_USERNAME") else None
mongo_password = config.get_env("MONGO_INITDB_ROOT_PASSWORD") if config.get_env("MONGO_INITDB_ROOT_PASSWORD") else None

mongo = Mongo(mongo_host, mongo_user, mongo_password, port=27017)

