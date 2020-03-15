# -*- coding: utf-8 -*-

"""Documentation file configuration.py."""

# =============================================================================
# IMPORTS
# =============================================================================

import os
from os import environ
from typing import NoReturn, Text
from settings.exception import ExceptionDefault

# =============================================================================
# CLASS - CONFIGURATION
# =============================================================================

class Configuration(ExceptionDefault):

    def __init__(self) -> NoReturn:
        self._envs = {"LOG_PATH": self._get_env_value("LOG_PATH"),
                        "LOG_FILE": self._get_env_value("LOG_FILE"),
                        "LOG_LEVEL": self._get_env_value("LOG_LEVEL"),
                        "LOGGER": self._get_env_value("LOGGER")}

    @staticmethod
    def _get_env_value(env: Text) -> Text:
        try:
            return environ.get(env)
        except KeyError as error:
            print(f"\nError to get the value of the environment variable {env} in the system - {error}")

    def _check_exist_env(self, env: Text) -> bool:
        return True if env in self._envs.keys() else False

    def get_env(self, env: Text) -> Text:
        check = lambda env: self._envs[env] if self._check_exist_env(env) else self.raise_exception(ValueError(f"The env {env} not exist in the default dict."))
        return check(env)
        