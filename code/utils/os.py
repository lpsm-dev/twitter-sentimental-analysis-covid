# -*- coding: utf-8 -*-

"""Documentation file os.py."""

# =============================================================================
# IMPORTS
# =============================================================================

from typing import NoReturn, Text
from os import path, makedirs

# =============================================================================
# CLASS - OS
# =============================================================================

class OS(object):

    @staticmethod
    def check_if_is_dir(directory: Text) -> bool:
        return True if path.isdir(directory) else False

    @staticmethod
    def check_if_is_file(file: Text) -> bool:
        return True if path.isfile(file) else False

    @staticmethod
    def join_directory_and_file(directory: Text, file: Text) -> Text:
        return str(path.join(directory, file))

    @staticmethod
    def create_directory(directory: Text) -> NoReturn:
        try:
            makedirs(directory)
        except OSError:
            print(f"\nError in create the directory {directory} in the system - {error}")
        except Exception as error:
            print(f"\nError general exception in create the directory {directory} in the system - {error}")

    @staticmethod
    def create_file(file: Text) -> NoReturn:
        try:
            with open(file, mode="w"): pass
        except Exception as error:
            print(f"\nError general exception create the file {file} in the system - {error}")
