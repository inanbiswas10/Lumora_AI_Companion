"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Context Builder

Description: Builds the complete conversation context before sending it to the language model.

Responsibilities:
    - Load recent conversation
    - Load user profile
    - Load relevant memories
    - Combine everything into one prompt

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""

class Context_Builder:

    def __init__ (self,database,memory_manager):

        self.database = database
        self.memory_manager = memory_manager

    def build_context_function (self,user_message):

        recent_messages = self.database.get_recent_messages_function (8)

        profile = self.database.get_all_user_profile_function ()

        memories = self.memory_manager.retrieve_relevant_memories_function (user_message)

        return {
            "recent_messages": recent_messages,
            "profile": profile,
            "memories": memories
        }