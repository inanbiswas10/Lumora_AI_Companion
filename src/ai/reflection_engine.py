"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Reflection Engine

Description: Analyzes Lumora's memories and user interactions to generate long-term insights about the user.

Responsibilities:
    - Reflect on stored memories
    - Discover user interests
    - Detect recurring emotions
    - Generate long-term insights
    - Store reflections

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""

from datetime import datetime

class Reflection_Engine:

    def __init__ (self,database):

        self.database = database

    def generate_reflection_function (self):

        memories = (
            self.database.get_conversation_memories_function ()
        )

        if len (memories) < 5:
            return None

        reflection = self._build_reflection (memories)

        self.database.save_conversation_memory_function (
            memory = reflection,
            importance = 10
        )
        return reflection

    def _build_reflection (self,memories):

        text = " ".join (memories).lower ()

        observations = []

        if "python" in text:
            observations.append (
                "The user enjoys Python programming."
            )

        if "ai" in text:
            observations.append (
                "The user is highly interested in Artificial Intelligence."
            )

        if "robot" in text or "humanoid" in text:
            observations.append (
                "The user wants to build a humanoid AI robot."
            )

        if "college" in text or "university" in text:
            observations.append (
                "Education is currently an important part of the user's life."
            )

        if "internship" in text:
            observations.append (
                "The user is actively preparing for a professional career."
            )

        if "github" in text:
            observations.append (
                "The user frequently works on software projects."
            )

        if len (observations) == 0:

            observations.append (
                "No significant long-term pattern detected yet."
            )

        today = datetime.now ().strftime ("%Y-%m-%d")

        reflection = (
            f"Reflection ({today}): "
            + " ".join (observations)
        )
        return reflection