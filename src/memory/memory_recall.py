"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Memory Recall

Description: Identifies when the user is asking Lumora to recall stored information.

Responsibilities:
    - Detect recall questions
    - Map questions to database keys
    - Support future natural language recall

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""

class Memory_Recall:
    
    # Handles memory recall requests.
    def recall_information_function (self,user_message):
      message = user_message.lower ().strip ()
      recall_patterns = {

          "what is my name":"name",
          "what's my name":"name",
          "what is my favourite colour":"favorite_colour",
          "what's my favourite colour":"favorite_colour",
          "where do i study":"university",
          "what is my hobby":"hobby",
          "what do i love":"interest"
      }
      return recall_patterns.get (message)