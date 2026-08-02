"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Preference Manager

Description: Handles user preferences and personal choices.

Responsibilities:
    - Detect user preferences
    - Save preferences
    - Retrieve preferences

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""

class Preference_Manager:
    def extract_preference_function (self,user_message):

        message = user_message.lower ().strip ()

        patterns = {

            "i prefer": "preference",

            "my favourite": "favorite",

            "my favorite": "favorite",

            "i like": "likes",

            "i don't like": "dislikes"
        }
        for phrase,key in patterns.items ():

            if message.startswith (phrase):

                value = user_message [len (phrase):].strip ()

                return key,value

        return None