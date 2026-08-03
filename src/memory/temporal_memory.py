"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Temporal Memory

Description: Extracts and resolves time-related information from user messages.

Responsibilities:
    - Detect temporal expressions
    - Resolve relative dates
    - Return normalized timestamps

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""
from datetime import datetime,timedelta


class Temporal_Memory:
    def extract_date_function(self, user_message):

        message = user_message.lower ()

        today = datetime.now ().date ()

        if "today" in message:
            return today

        if "tomorrow" in message:
            return today + timedelta (days = 1)

        if "yesterday" in message:
            return today - timedelta (days = 1)
        return None