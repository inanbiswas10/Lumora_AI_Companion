"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Gemini Provider

Description: Communicates with Google's Gemini model to generate intelligent responses.

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""

from google import genai
from config.api_keys import GEMINI_API_KEY
from src.llm.provider import LLM_Provider

class Gemini_Provider (LLM_Provider):
    
    # Google Gemini implementation of the LLM provider.
    def __init__ (self):
       self.client = genai.Client (api_key=GEMINI_API_KEY)

    def generate_response_function (self,prompt):
      response = self.client.models.generate_content (model="openrouter/free",contents=prompt)
      return response.text