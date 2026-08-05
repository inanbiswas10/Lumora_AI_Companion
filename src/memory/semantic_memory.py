"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Semantic Memory

Description: Retrieves memories that are relevant to the current conversation.

Responsibilities:
    - Search relevant memories
    - Prepare for embedding search
    - Support future vector databases

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""

class Semantic_Memory:

    def __init__ (self,database):
        self.database = database

    def retrieve_relevant_memories_function (self,user_message):

        user_message = user_message.lower ()

        memories = self.database.get_conversation_memories_function ()

        relevant = []

        for memory in memories:

            if any (word in memory.lower ()
                    
                   for word in user_message.split ()):

                relevant.append(memory)
        return relevant