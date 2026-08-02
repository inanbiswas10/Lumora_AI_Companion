"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Context Builder

Description: Collects all contextual information required for AI response generation.

Responsibilities:
    - Fetch user profile
    - Fetch recent conversation
    - Fetch relevant memories (future)
    - Detect emotion

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""

class Context_Builder:

    def __init__ (self,database,emotion_detector,semantic_memory):

        self.database = database
        self.emotion_detector = emotion_detector
        self.semantic_memory = semantic_memory

    def build_context_function (self,user_message):

        context = {

            "user_profile":
                self.database.get_all_user_profile_function (),

            "conversation_history":
                self.database.get_recent_messages_function (limit = 10),

            "relevant_memories":
                self.semantic_memory.retrieve_relevant_memories_function (
                    user_message
                ),

            "emotion":
                self.emotion_detector.detect_emotion_function (
                    user_message
                )
        }
        return context