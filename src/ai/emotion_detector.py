"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Emotion Detector

Description: Detects the emotional tone of the user's message.

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""

class Emotion_Detector:
    
    # Detects basic emotions from user messages.

    def detect_emotion_function (self,message):
      message = message.lower ()

      happy_words = [
          "happy",
          "great",
          "awesome",
          "excited",
          "wonderful",
          "fantastic",
          "good",
          "joy"
      ]
      sad_words = [
          "sad",
          "depressed",
          "upset",
          "cry",
          "hurt",
          "lonely",
          "miserable"
      ]
      angry_words = [
          "angry",
          "furious",
          "annoyed",
          "mad",
          "hate",
          "frustrated"
      ]
      anxious_words = [
          "anxious",
          "worried",
          "nervous",
          "stress",
          "panic",
          "afraid"
      ]
      for word in happy_words:
          if word in message:
              return "Happy"

      for word in sad_words:
          if word in message:
              return "Sad"

      for word in angry_words:
          if word in message:
              return "Angry"

      for word in anxious_words:
        if word in message:
            return "Anxious"
      return "Neutral"