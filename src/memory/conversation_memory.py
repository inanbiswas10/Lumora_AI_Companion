"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Conversation Memory

Description: Stores important conversation memories for future recall.

Responsibilities:
    - Save important user messages
    - Retrieve stored memories
    - Prepare for semantic memory integration

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""

class Conversation_Memory:
    
    def __init__ (self,database):

         self.database = database

    def should_store_function (self,user_message):

        """
        Decide whether this message is important enough
        to remember permanently.
        """

        message = user_message.lower()

        important_keywords = [

            "today",

            "tomorrow",

            "yesterday",

            "interview",

            "exam",

            "birthday",

            "family",

            "friend",

            "job",

            "college"
        ]
        return any (word in message for word in important_keywords)