# -*- coding: utf-8 -*-

from flask_restplus import Api

from typing import NoReturn, Callable

# ==============================================================================
# GLOBAL
# ==============================================================================

api = Api(version="1.0",
        prefix="",
        title="Sentimental Analysis API",
        description="Swagger domumentation from Sentimental Analysis API",
        contact="Lucca Pessoa da Silva Matos",
        contact_email="luccapsm@gmail.com",
        doc="/documentation")

ns_tweets = api.namespace("tweets", description="Tweets operations")

responses = {200: "Successful operation",
             400: "Invalid status value",
             404: "The server could not find the requested resource (Not Found)",
             500: "Unexpected condition (Internal Server Error)"}

# ==============================================================================
# FUNCTIONS
# ==============================================================================

def configure(app: Callable) -> NoReturn:
  api.init_app(app)
  app.api = api
