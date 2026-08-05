"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Personality Evolution

Description: Maintains Lumora's long-term personality profile and gradually adapts its communication style based on user interactions while preserving its core identity.

Responsibilities:
    - Store personality traits
    - Update communication style
    - Track conversation statistics
    - Build adaptive personality prompt
    - Prepare future learning

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""

class Personality_Evolution:

    def __init__ (self):

        self.personality = {

            "kindness": 10,

            "empathy": 10,

            "humor": 5,

            "professionalism": 8,

            "playfulness": 5,

            "curiosity": 8,

            "supportiveness": 10,

            "confidence": 8

        }

        self.statistics = {

            "total_conversations": 0,

            "happy_messages": 0,

            "sad_messages": 0,

            "angry_messages": 0,

            "neutral_messages": 0

        }

    # --------------------------------------------------------

    def record_conversation_function (
        self,
        emotion
    ):

        self.statistics ["total_conversations"] += 1

        if emotion == "happy":
            self.statistics ["happy_messages"] += 1

        elif emotion == "sad":
            self.statistics ["sad_messages"] += 1

        elif emotion == "angry":
            self.statistics ["angry_messages"] += 1

        else:
            self.statistics ["neutral_messages"] += 1

    # --------------------------------------------------------

    def adjust_trait_function (
        self,
        trait,
        amount
    ):

        if trait not in self.personality:
            return

        self.personality [trait] += amount

        self.personality [trait] = max (
            1,
            min (
                10,
                self.personality [trait]
            )
        )

    # --------------------------------------------------------

    def get_personality_function (self):

        return self.personality

    # --------------------------------------------------------

    def build_personality_prompt_function (self):

        prompt = f"""

Current Personality

Kindness : {self.personality ['kindness']}/10
Empathy : {self.personality ['empathy']}/10
Humor : {self.personality ['humor']}/10
Professionalism : {self.personality ['professionalism']}/10
Playfulness : {self.personality ['playfulness']}/10
Curiosity : {self.personality ['curiosity']}/10
Supportiveness : {self.personality ['supportiveness']}/10
Confidence : {self.personality ['confidence']}/10

Always preserve Lumora's caring, intelligent,
honest and respectful personality.

"""

        return prompt

    # --------------------------------------------------------

    def get_statistics_function (self):

        return self.statistics