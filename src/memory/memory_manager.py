"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Memory Manager

Description: Coordinates every memory-related operation inside Lumora AI.

Responsibilities:
    - Extract memories
    - Store memories
    - Retrieve semantic memories
    - Calculate importance
    - Update memories
    - Forget memories (future)

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""
class Memory_Manager:

    def __init__ (self,database,memory_extractor,memory_recall,semantic_memory,conversation_memory,semantic_retriever,importance_analyzer):
        self.database = database
        self.memory_extractor = memory_extractor
        self.memory_recall = memory_recall
        self.semantic_memory = semantic_memory
        self.conversation_memory = conversation_memory
        self.semantic_retriever = semantic_retriever
        self.importance_analyzer = importance_analyzer

    def retrieve_relevant_memories_function (self,user_message):
        return self.semantic_retriever.retrieve_relevant_memories_function (user_message)