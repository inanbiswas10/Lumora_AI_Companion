"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Emotion Detector

Description: Detects the emotional state of the user from messages.

Responsibilities:
    - Detect emotions
    - Estimate confidence
    - Prepare for AI emotion models

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""

class Emotion_Detector:

    def detect_emotion_function (self,user_message):

        message = user_message.lower ()

        emotions = {

            "happy": [
                "happy",
                "great",
                "awesome",
                "excited",
                "amazing",
                "love"
            ],

            "sad": [
                "sad",
                "cry",
                "lonely",
                "hurt",
                "depressed",
                "broken"
            ],

            "angry": [
                "angry",
                "hate",
                "annoyed",
                "furious",
                "mad"
            ],

            "fear": [
                "afraid",
                "scared",
                "worried",
                "anxious",
                "nervous"
            ]
        }
        for emotion,words in emotions.items ():

            for word in words:

                if word in message:

                    return (
                        emotion,
                        0.95
                    )
        return (
            "neutral",
            0.60
        )