"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Memory Recall

Description: Identifies when the user is asking Lumora to recall stored information.

Responsibilities:
    - Detect recall questions
    - Retrieve stored memories
    - Support future NLP-based recall

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""

class Memory_Recall:

    def __init__ (self,database):

        self.database = database

    def recall_information_function (self,user_message):

        message = user_message.lower ().strip ()

        recall_patterns = {

            "what is my name": "name",
            "what's my name": "name",

            "what is my favourite colour": "favorite_colour",
            "what's my favourite colour": "favorite_colour",

            "where do i study": "university",

            "what is my hobby": "hobby",

            "what do i love": "interest"
        }
        key = recall_patterns.get (message)

        if key is None:
            return None
        value = self.database.get_user_profile_function (key)

        if value is None:
            return None
        return key,value