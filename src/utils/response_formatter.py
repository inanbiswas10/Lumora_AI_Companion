"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Response Formatter

Description: Formats AI responses before displaying them.

Responsibilities:
    - Improve readability
    - Add paragraph spacing
    - Clean unnecessary whitespace

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""

import re

class Response_Formatter:

    def format_response_function (self,response):

        # Remove extra spaces
        response = re.sub (r"\s+"," ",response).strip ()

        # Add a blank line after sentence endings
        response = re.sub (r"([.!?])\s+",r"\1\n\n",response)
        return response