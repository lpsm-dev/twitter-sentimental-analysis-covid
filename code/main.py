# -*- coding: utf-8 -*-

"""Documentation file __init__.py."""

# =============================================================================
# IMPORTS
# =============================================================================

from settings.log import Log
from actions.twitter import Functions
from settings.configuration import Configuration

# =============================================================================

import sys
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format

# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":

    cprint(figlet_format("API", font="starwars"), "red", "on_yellow", attrs=["dark"])

    config = Configuration()

    log_path = config.get_env("LOG_PATH") if config.get_env("LOG_PATH") else None
    log_file = config.get_env("LOG_FILE") if config.get_env("LOG_FILE") else None

    log = Log(log_path, log_file, config.get_env("LOG_LEVEL"), config.get_env("LOGGER")).logger

    log.info("Getting information")

    query = {'q': 'Corona',
        'result_type': 'mixed',
        'count': 100,
        'lang': 'pt',
        }

    resultados = Functions(log).search(**query)

    for tweet in resultados:
        print(f"Tweet: {tweet.text}\n")
