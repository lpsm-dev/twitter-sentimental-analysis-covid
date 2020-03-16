# -*- coding: utf-8 -*-

"""Documentation file __init__.py."""

# =============================================================================
# IMPORTS
# =============================================================================

from flask import Flask
from flask_cors import CORS
from .restplus import configure as config_api
from .endpoints.tweets.routes import ns_tweets
from app.settings.configuration import Configuration

# =============================================================================
# GLOBAL
# =============================================================================

config = Configuration()

# =============================================================================
# FUNCTIONS
# =============================================================================

def create_app(config_filename=None):
    app = Flask(__name__, instance_relative_config=True)
    _ = CORS(app, resources={r"*": {"origins": "*"}})
    config_api(app)

    app.api.add_namespace(ns_tweets)

    register_blueprints(app)
    app.config.from_object(Configuration)
    return app

# =============================================================================

def register_blueprints(app):
    from app.endpoints import api_blueprint
    app.register_blueprint(api_blueprint)
