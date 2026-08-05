"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Reasoning Engine

Description: Determines how Lumora should respond before calling the language model.

Responsibilities:
    - Detect memory recall requests
    - Detect emotional situations
    - Decide whether memory retrieval is required
    - Select the response strategy
    - Prepare for future planning and tool usage

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""

class Reasoning_Engine:

    def __init__ (
        self,
        memory_recall,
        emotion_detector
    ):

        self.memory_recall = memory_recall
        self.emotion_detector = emotion_detector

    def analyze_message_function (
        self,
        user_message
    ):

        strategy = {

            "requires_memory_recall": False,

            "memory_key": None,

            "emotion": "neutral",

            "response_mode": "conversation"

        }

        # ----------------------------------------
        # Detect memory recall
        # ----------------------------------------

        memory_key = (
            self.memory_recall
            .recall_information_function (user_message)
        )

        if memory_key:

            strategy ["requires_memory_recall"] = True
            strategy ["memory_key"] = memory_key
            strategy ["response_mode"] = "memory"

        # ----------------------------------------
        # Detect emotion
        # ----------------------------------------

        emotion = (
            self.emotion_detector
            .detect_emotion_function (user_message)
        )

        strategy ["emotion"] = emotion

        # ----------------------------------------
        # Emotional response priority
        # ----------------------------------------

        if emotion in [

            "sad",
            "fear",
            "angry"

        ]:

            strategy ["response_mode"] = "empathy"

        return strategy