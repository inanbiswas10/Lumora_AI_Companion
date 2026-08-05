"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Emotion State

Description: Maintains Lumora's current emotional state.

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""
class Emotion_State:

    def __init__ (self):

        self.current_emotion = "calm"

    def set_emotion_function (self,emotion):

        self.current_emotion = emotion

    def get_emotion_function (self):

        return self.current_emotion