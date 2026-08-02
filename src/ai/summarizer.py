"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Conversation Summarizer

Description: Generates concise summaries of previous conversations.

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""

class Conversation_Summarizer:
    
    # Creates simple summaries from conversation history.

    def summarize_function (self,history):

      if not history:
        return "We haven't had any conversations yet."
      summary = "Here's a summary of our recent conversations:\n\n"

      for speaker,message in history:
        summary += f"• {speaker}: {message}\n"
      return summary