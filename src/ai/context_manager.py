"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Context Manager

Description: Builds the complete conversational context before Lumora generates a response.

Responsibilities:
    - Retrieve user profile
    - Retrieve recent conversations
    - Retrieve relevant memories
    - Detect emotion
    - Retrieve recent episodes

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

    # ---------------------------------------------------------

    def build_context_function (
        self,
        user_message
    ):

        # ---------------- Emotion ----------------

        emotion, confidence = (
            self.emotion_detector
            .detect_emotion_function (
                user_message
            )
        )

        # ---------------- User Profile ----------------

        profile = (
            self.memory_manager
            .get_user_profile_function ()
        )

        # ---------------- Conversation History ----------------

        recent_messages = (
            self.memory_manager
            .get_recent_conversations_function (
                limit = 10
            )
        )

        # ---------------- Relevant Memories ----------------

        memories = (
            self.memory_manager
            .retrieve_relevant_memories_function (
                user_message
            )
        )

        # ---------------- Episodes ----------------

        episodes = (
            self.database
            .get_recent_episodes_function ()
        )

        return {

            "emotion": emotion,

            "confidence": confidence,

            "profile": profile,

            "recent_messages": recent_messages,

            "memories": memories,

            "episodes": episodes

        }