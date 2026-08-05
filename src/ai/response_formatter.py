"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Response Formatter

Description: Formats every AI response before it is shown to the user.

Responsibilities:
    - Remove unnecessary whitespace
    - Normalize line breaks
    - Capitalize sentences
    - Prepare future markdown support
    - Prepare future emoji control
    - Keep responses natural and readable

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""
import re

class Response_Formatter:

    def __init__ (self):
        pass


    def format_response_function (self,response):

        if response is None:
            return ""

        response = response.strip ()

        # Remove multiple spaces
        response = re.sub (r"\s+"," ",response)

        # Remove excessive blank lines
        response = re.sub (r"\n{3,}", "\n\n",response)

        # Capitalize first character
        if len (response) > 0:
            response = response [0].upper () + response [1:]

        return response

    def clean_stream_chunk_function (self,chunk):

        if chunk is None:
            return ""

        return chunk.replace ("\r","")

    def finalize_response_function (self,response):

        response = self.format_response_function (response)

        return response