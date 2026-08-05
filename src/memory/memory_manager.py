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

    def process_user_message_function (self,user_message):

        memory = self.memory_extractor.extract_information_function (user_message)

        if memory is None:
            return

        importance = self.importance_analyzer.calculate_importance_function (memory)

        self.semantic_memory.store_memory_function (memory,importance)

    def recall_user_information_function (self,user_message):

        key = self.memory_recall.recall_information_function (user_message)

        if key is None:
            return None

        value = self.database.get_user_profile_function (key)

        if value is None:
            return None
        return value

    