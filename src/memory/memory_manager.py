"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Memory Manager

Description: Coordinates every memory-related operation inside Lumora AI.

Responsibilities:
    - Extract profile memories
    - Store semantic memories
    - Retrieve relevant memories
    - Recall user information
    - Calculate memory importance

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""


class Memory_Manager:

    def __init__ ( 
        self,
        database,
        memory_extractor,
        memory_recall,
        semantic_memory,
        conversation_memory,
        semantic_retriever,
        importance_analyzer
    ):

        self.database = database
        self.memory_extractor = memory_extractor
        self.memory_recall = memory_recall
        self.semantic_memory = semantic_memory
        self.conversation_memory = conversation_memory
        self.semantic_retriever = semantic_retriever
        self.importance_analyzer = importance_analyzer

    # ---------------------------------------------------------

    def process_user_message_function (self,user_message):

        """
        Extract profile information from the user's message
        and store it in both the user profile and semantic memory.
        """

        memory = self.memory_extractor.extract_information_function (
            user_message
        )

        if memory is None:
            return

        key,value = memory

        # ---------------- Save User Profile ----------------

        self.database.save_user_profile_function (
            key,
            value
        )

        # ---------------- Calculate Importance ----------------

        importance = (
            self.importance_analyzer
            .calculate_importance_function (key)
        )

        # ---------------- Store Semantic Memory ----------------

        self.semantic_memory.store_memory_function (
            memory,
            importance
        )

    # ---------------------------------------------------------

    def retrieve_relevant_memories_function (
        self,
        user_message
    ):

        """
        Retrieve memories that are relevant to
        the current conversation.
        """

        return (
            self.semantic_retriever
            .retrieve_relevant_memories_function (
                user_message
            )
        )

    # ---------------------------------------------------------

    def recall_user_information_function (
        self,
        user_message
    ):

        """
        Recall stored user profile information.
        """

        key = (
            self.memory_recall
            .recall_information_function (
                user_message
            )
        )

        if key is None:
            return None

        value = (
            self.database
            .get_user_profile_function (
                key
            )
        )

        return value

    # ---------------------------------------------------------

    def get_user_profile_function (self):

        """
        Return the complete user profile.
        """

        return (
            self.database
            .get_all_user_profile_function ()
        )

    # ---------------------------------------------------------

    def get_recent_conversations_function (
        self,
        limit = 10
    ):

        """
        Return recent conversations.
        """

        return (
            self.database
            .get_recent_messages_function (
                limit
            )
        )