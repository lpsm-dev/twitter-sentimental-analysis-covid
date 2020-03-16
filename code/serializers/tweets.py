# -*- coding: utf-8 -*-

"""Documentation file tweets.py."""

# =============================================================================
# IMPORTS
# =============================================================================

from app.restplus import api
from flask_restplus import fields

# =============================================================================
# FUNCTIONS
# =============================================================================

tweets_serializer = api.model("Tweets",{
                "phrase": fields.String(required=True),
                "count": fields.Integer(required=False),
                "result_type": fields.String(required=False),
                "language": fields.String(required=True)
            })
