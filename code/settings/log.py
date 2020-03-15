# -*- coding: utf-8 -*-

"""Documentation file log.py."""

# =============================================================================
# IMPORTS
# =============================================================================

import sys
import logging
import coloredlogs
import logging.config
from utils.os import OS
from typing import NoReturn, Text
from pythonjsonlogger import jsonlogger

# =============================================================================
# CLASS - LOG
# =============================================================================

class Log(OS):

    def __init__(self, log_path: Text, log_file: Text, log_level: Text, logger_name: Text) -> NoReturn:
        self._log_path = log_path if log_path else "/var/log/sentiment-analysis"
        self._log_file = self.join_directory_and_file(log_path, log_file if log_file else "file.log")

        self._check_log_path_and_log_file()

        self._log_level = self._check_log_level(log_level)
        self._logger_name = logger_name

        self.formatter = "%(levelname)s - %(asctime)s - %(message)s - %(pathname)s - %(funcName)s"

        self._logger = logging.getLogger(self._logger_name)

        self._logger.setLevel(self._log_level)
        self._base_configuration_log_colored()
        self._logger.addHandler(self._base_configuration_log_file())

    @staticmethod
    def _check_log_level(level: Text) -> Text:
        return level if level in ["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG", "NOTSET"] else None

    def _check_log_path_and_log_file(self) -> NoReturn:
        if self.check_if_is_dir(self.log_path):
            print(f"\nThe log path {self.log_path} alredy exist in the system")
            if self.check_if_is_file(self.log_file):
                print(f"\nThe log file {self.log_file} alredy exist in the system... Everything is okay")
            else:
                self.create_file(self.log_file)
        else:
            self.create_directory(self.log_path)
            self.create_file(self.log_file)

    def _base_configuration_log_colored(self) -> coloredlogs.install:
        try:
            coloredlogs.install(
                level=self._log_level,
                logger=self._logger,
                fmt=self.formatter,
                milliseconds=True)
        except Exception as error:
            print(f"\nError general exception in create a base configuration colored to use in log file - {error}")

    def _base_configuration_log_file(self) -> logging.FileHandler:
        try:
            file_handler = logging.FileHandler(
            filename=f"{self._log_file}")
            file_handler.setLevel(self._log_level)
            file_handler.setFormatter(jsonlogger.JsonFormatter(self.formatter))
            return file_handler if file_handler else None
        except Exception as error:
            print(f"\nError general exception in create the base configuration to used log file - {error}")

    @property
    def log_path(self) -> Text:
        return self._log_path

    @property
    def log_file(self) -> Text:
        return self._log_file

    @property
    def log_level(self) -> Text:
        return self._log_level

    @property
    def logger_name(self) -> Text:
        return self._logger_name

    @property
    def logger(self) -> Text:
        return self._logger
        