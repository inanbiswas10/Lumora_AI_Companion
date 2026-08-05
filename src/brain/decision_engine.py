"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Decision Engine

Description: Decides what action Lumora should perform after the message has been analyzed by the Reasoning Engine.

Responsibilities:
    - Handle memory recall
    - Handle empathetic conversations
    - Handle normal conversations
    - Prepare for future tools
    - Prepare for future web search
    - Prepare for future planning

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""
class Decision_Engine:

    def __init__ (
        self,
        database,
        reasoning_engine
    ):

        self.database = database
        self.reasoning_engine = reasoning_engine

    def decide_function (
        self,
        user_message
    ):

        strategy = (
            self.reasoning_engine
            .analyze_message_function (user_message)
        )

        response_mode = strategy ["response_mode"]

        # ------------------------------------------------
        # Memory Recall
        # ------------------------------------------------

        if response_mode == "memory":

            value = (
                self.database
                .get_user_profile_function (
                    strategy ["memory_key"]
                )
            )

            if value:

                return {

                    "action": "direct_response",

                    "response":
                        f"You told me that your "
                        f"{strategy ['memory_key'].replace('_',' ')} "
                        f"is {value}."

                }

            return {

                "action": "direct_response",

                "response":
                    "I don't remember that information yet."

            }

        # ------------------------------------------------
        # Emotional Support
        # ------------------------------------------------

        if response_mode == "empathy":

            return {

                "action": "llm",

                "emotion": strategy ["emotion"]

            }

        # ------------------------------------------------
        # Normal Conversation
        # ------------------------------------------------

        return {

            "action": "llm",

            "emotion": strategy ["emotion"]

        }