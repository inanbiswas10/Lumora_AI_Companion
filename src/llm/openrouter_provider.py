"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: OpenRouter Provider

Description: Communicates with OpenRouter to generate intelligent AI responses.

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""

import requests
from config.api_keys import OPENROUTER_API_KEY
from src.llm.provider import LLM_Provider

class OpenRouter_Provider (LLM_Provider):

    def __init__ (self):

      self.url = "https://openrouter.ai/api/v1/chat/completions"

      self.headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
    }
    def generate_response_function (self,prompt):

      payload = {
            "model":"openai/gpt-4.1-mini",
            "messages": [
                {
                    "role":"user",
                    "content":prompt
                }
            ]
      }
      response = requests.post (
            self.url,
            headers=self.headers,
            json=payload
      )
      response.raise_for_status ()
      data = response.json()
      return data["choices"][0]["message"]["content"]

