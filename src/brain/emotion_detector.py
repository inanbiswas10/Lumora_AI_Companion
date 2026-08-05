"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Emotion Detector

Description: Detects the emotional state of the user from their message.

Responsibilities:
    - Detect emotions
    - Estimate confidence
    - Support future AI emotion models

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
                "great",
                "awesome",
                "excited",
                "amazing",
                "fantastic",
                "wonderful"
            ],

            "sad": [
                "sad",
                "depressed",
                "cry",
                "lonely",
                "upset",
                "hurt"
            ],

            "angry": [
                "angry",
                "mad",
                "furious",
                "annoyed"
            ],

            "fear": [
                "afraid",
                "scared",
                "worried",
                "anxious",
                "nervous"
            ],

            "love": [
                "love",
                "care",
                "miss",
                "hug"
            ]
        }
        for emotion,keywords in emotion_keywords.items ():

            for keyword in keywords:

                if keyword in message:

                    return emotion
        return "neutral"