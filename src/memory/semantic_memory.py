"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Semantic Memory

Description: Stores and retrieves semantic memories that Lumora can use during future conversations.

Responsibilities:
    - Store semantic memories
    - Retrieve relevant memories
    - Support future embedding search

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""

class Semantic_Memory:

    def __init__ (self,database):

        self.database = database

    # ---------------------------------------------------------

    def store_memory_function (
        self,
        memory,
        importance = 5
    ):

        """
        Store a semantic memory.
        """

        if isinstance (memory,tuple):

            key,value = memory

            memory_text = f"{key}: {value}"

        else:

            memory_text = str (memory)

        self.database.save_conversation_memory_function (
            memory_text,
            importance
        )

    # ---------------------------------------------------------

    def retrieve_relevant_memories_function (
        self,
        user_message
    ):

        """
        Placeholder implementation.

        Later this will use embeddings and cosine similarity.

        For now it simply returns the most recent stored memories.
        """

        memories = (
            self.database
            .get_conversation_memories_function ()
        )

        return memories [:5]