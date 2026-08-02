"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Groq Provider

Description: Communicates with the Groq API to generate intelligent AI responses.

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""
from groq import Groq
from config.api_keys import GROQ_API_KEY
from src.llm.provider import LLM_Provider

class Groq_Provider (LLM_Provider):
    def __init__ (self):
      self.client = Groq (api_key=GROQ_API_KEY)

    def generate_response_function (self,prompt):

        response = self.client.chat.completions.create (

            model="llama-3.3-70b-versatile",

            messages=[
                {
                    "role":"user",
                    "content":prompt
                }
            ]
        )
        return response.choices[0].message.content