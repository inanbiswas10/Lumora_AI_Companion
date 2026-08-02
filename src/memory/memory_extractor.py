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
    
    # Extract important information from user messages.
    def extract_information_function (self,user_message):
        message = user_message.lower ().strip ()
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
        for key,phrases in patterns.items ():
            for phrase in phrases:
                if message.startswith(phrase):
                    value = user_message [len (phrase):].strip ()
                    return (key,value)