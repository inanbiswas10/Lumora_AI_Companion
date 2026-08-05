"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Emotional Memory

Description: Stores and retrieves the user's emotional history.

Responsibilities:
    - Store detected emotions
    - Retrieve recent emotional history
    - Support future emotion trends

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""

from datetime import datetime

class Emotional_Memory:

    def __init__ (self,database):

        self.database = database


    def store_emotion_function (self,emotion):

        timestamp = datetime.now ().strftime ("%Y-%m-%d %H:%M:%S")

        self.database.save_emotion_function (emotion,timestamp)

    def get_recent_emotions_function (self,limit = 10):

        return self.database.get_recent_emotions_function (limit)