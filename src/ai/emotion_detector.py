"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Emotion Detector

Description: Detects the emotional state of the user from messages.

Responsibilities:
    - Detect emotion
    - Return confidence score
    - Support future AI-based emotion analysis

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""

class Emotion_Detector:

    def detect_emotion_function (self,user_message):

        message = user_message.lower ()

        emotion_keywords = {

            "happy": [
                "happy",
                "excited",
                "great",
                "awesome",
                "amazing",
                "wonderful",
                "good news",
                "finally",
                "won",
                "success"
            ],

            "sad": [
                "sad",
                "cry",
                "depressed",
                "lonely",
                "hurt",
                "miss",
                "upset",
                "heartbroken"
            ],

            "angry": [
                "angry",
                "mad",
                "annoyed",
                "hate",
                "furious"
            ],

            "fear": [
                "afraid",
                "fear",
                "scared",
                "nervous",
                "worried",
                "anxious"
            ],

            "surprised": [
                "wow",
                "unexpected",
                "can't believe",
                "really",
                "seriously"
            ]
        }
        for emotion,keywords in emotion_keywords.items ():

            for keyword in keywords:

                if keyword in message:

                    return emotion,0.90
        return "neutral",0.50