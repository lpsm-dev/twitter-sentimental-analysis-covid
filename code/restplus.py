# -*- coding: utf-8 -*-

"""Documentation file restplus.py."""

# =============================================================================
# IMPORTS
# =============================================================================

from flask_restplus import Api
from typing import NoReturn, Callable

# =============================================================================
# IMPORTS
# =============================================================================

api = Api(version="1.0", 
        prefix="",
        title="Sentimental Analysis API",
        description="Swagger domumentation from Sentimental Analysis API",
        contact="Lucca Pessoa da Silva Matos",
        contact_email="luccapsm@gmail.com",
        doc="/documentation")

# =============================================================================
# IMPORTS
# =============================================================================

def configure(app: Callable) -> NoReturn:
    api.init_app(app)
    app.api = api
