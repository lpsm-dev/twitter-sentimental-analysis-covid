# -*- coding: utf-8 -*-

from model.mongo import Mongo
from variables.general import config

# ==============================================================================
# GLOBAL
# ==============================================================================

mongo_host = config.get_env("MONGO_HOST")
mongo_port=27017
mongo_user = config.get_env("MONGO_INITDB_ROOT_USERNAME")
mongo_password = config.get_env("MONGO_INITDB_ROOT_PASSWORD")

mongo = Mongo(mongo_host, mongo_user, mongo_password, port=mongo_port)
