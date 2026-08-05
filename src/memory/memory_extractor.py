"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Memory Extractor

Description: Extracts important personal information from user conversations.

Responsibilities:
    - Detect user profile information
    - Extract key-value pairs
    - Support future NLP-based memory extraction

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""

class Memory_Extractor:
    
    def extract_information_function (self,user_message):

        original_message = user_message.strip ()
        message = original_message.lower ()

        patterns = {
            "name": [
                "my name is",
                "i am",
                "i'm",
                "people call me",
                "my friends call me",
                "you can call me"
            ],

        "favorite_colour": [
            "my favourite colour is",
            "my favorite colour is",
            "my favourite color is",
            "my favorite color is"
            ],

        "university": [
            "i study at",
            "i study in",
            "i am studying at"
            ],

        "workplace": [
            "i work at",
            "i work for"
            ],

        "hobby": [
            "my hobby is",
            "my hobbies are"
            ],

        "interest": [
            "i love",
            "i enjoy",
            "i'm interested in"
            ]
        }
        for key,phrases in patterns.items():

            for phrase in phrases:

                if message.startswith (phrase):

                    value = original_message [len (phrase):].strip()

                    if value:
                        return (key,value)
        return None