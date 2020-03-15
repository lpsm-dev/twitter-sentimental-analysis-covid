# -*- coding: utf-8 -*-

"""Documentation file twitter.py."""

# =============================================================================
# IMPORTS
# =============================================================================

from typing import Callable
from app.restplus import api

# =============================================================================
# FUNCTIONS
# =============================================================================

def ns_twitter() -> Callable:
    return api.namespace("twitter", description="Twitter operations")
    