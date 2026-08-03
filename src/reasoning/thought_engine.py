"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Thought Engine

Description: Performs internal reasoning before generating a response.

Responsibilities:
    - Understand the user's intent
    - Consider emotion
    - Consider memories
    - Generate an internal thought

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""
class Thought_Engine:

    def think_function (self,user_message,emotion,memories):

        thought = []
        thought.append (f"User emotion: {emotion}")
        thought.append (f"Relevant memories found: {len (memories)}")
        thought.append (f"Current message: {user_message}")
        return "\n".join (thought)