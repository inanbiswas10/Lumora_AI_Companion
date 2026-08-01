"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Logger

Description: This module provides logging utilities for Lumora AI.

Responsibilities:
    - Record application events
    - Log errors and warnings
    - Support debugging
    - Maintain execution logs

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""

from datetime import datetime

class Logger:

    # A simple logger for Lumora AI.
    # This class provides methods to display formatted log messages
    # with timestamps and different severity levels.

    def _log_function (self,level:str,message:str):

        # Display a formatted log message.
        # Args:
        # level (str): Log level (INFO,WARNING,ERROR etc)
        # message (str): Message to display.

        current_time = datetime.now ().strftime ("%Y-%m-%d %H:%M:%S")

        print (f"{current_time} | {level:<5}| {message}")
        print ()

    def info_function (self,message:str):

        # Display an informational message.

        self._log_function ("INFO",message)

    def warning_function (self,message:str):

        # Display a warning message.

        self._log_function ("WARNING",message)

    def error_function (self,message:str):

        # Display an error message.

        self._log_function ("ERROR",message)

    def critical_function (self,message:str):
        # Display a critical message.

        self._log_function ("CRITICAL",message)



