# -*- coding: utf-8 -*-

"""Documentation file twitter.py."""

# =============================================================================
# IMPORTS
# =============================================================================

from typing import Callable
from app.restplus import api
from flask_restplus import fields

# =============================================================================
# FUNCTIONS
# =============================================================================

def twitter_serializer() -> Callable:
    return api.model("Twitter",{
                "phrase": fields.String(required=True),
                "language": fields.String(required=True)
            })
