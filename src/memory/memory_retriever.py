"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Memory Retriever

Description: Retrieves relevant memories from the database before generating a response.

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""

class Memory_Retriever:
    def __init__ (self,database):
        self.database = database

    def retrieve_memories_function (self,limit = 5):
        
        """
        Returns the most recent stored conversation memories.
        Later this will use semantic search.
        """
        return self.database.get_conversation_memories_function ()[:limit]