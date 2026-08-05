"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Context Manager

Description: Collects every piece of information required before generating an AI response.

Responsibilities:
    - Load user profile
    - Load recent conversation
    - Load memories
    - Detect emotion
    - Return a complete context dictionary

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""

class Context_Manager:

    def __init__ (
        self,
        database,
        memory_manager,
        emotion_detector
    ):

        self.database = database
        self.memory_manager = memory_manager
        self.emotion_detector = emotion_detector

    def build_context_function (self, user_message):

        profile = self.database.get_all_user_profile_function ()

        recent_messages = (
            self.database
            .get_recent_messages_function (limit = 10)
        )

        memories = (
            self.memory_manager
            .retrieve_relevant_memories_function (
                user_message
            )
        )

        emotion = (
            self.emotion_detector
            .detect_emotion_function (
                user_message
            )
        )

        context = {

            "profile": profile,

            "recent_messages": recent_messages,

            "memories": memories,

            "emotion": emotion
        }
        return context