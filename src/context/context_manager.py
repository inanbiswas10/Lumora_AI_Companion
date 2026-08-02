"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Context Manager

Description: Collects all information required to generate an AI response.

Responsibilities:
    - Fetch user profile
    - Fetch recent conversation
    - Detect emotion

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""

class Context_Manager:
    
    def __init__ (self,database,emotion_detector):

        self.database = database
        self.emotion_detector = emotion_detector

    def build_context_function (self,user_message):

        user_profile = self.database.get_all_user_profile_function ()

        conversation_history = self.database.get_recent_messages_function (limit = 10)

        emotion = self.emotion_detector.detect_emotion_function (user_message)

        return {
            "user_profile": user_profile,
            "conversation_history": conversation_history,
            "emotion": emotion
        }