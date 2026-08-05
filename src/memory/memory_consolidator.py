"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Memory Consolidator

Description: Creates long-term memories by summarizing recent conversations.

Responsibilities:
    - Read recent conversations
    - Generate meaningful long-term memories
    - Store summarized memories

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""

from src.ai.summarizer import Conversation_Summarizer

class Memory_Consolidator:

    def __init__ (self,database):

        self.database = database
        self.summarizer = Conversation_Summarizer ()

    def consolidate_recent_memory_function (self):

        history = self.database.get_recent_messages_function (limit = 20)

        if len (history) < 6:
            return

        summary = self.summarizer.summarize_function (history)

        self.database.save_conversation_memory_function (
            memory = summary,
            importance = 9
        )
        return summary