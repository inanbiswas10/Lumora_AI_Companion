"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Conversation Service

Description: Acts as the bridge between the UI and Lumora's AI Engine.

Responsibilities:
    - Receive user messages
    - Handle memory recall requests
    - Handle conversation history requests
    - Handle conversation summary requests
    - Delegate AI response generation

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""

from src.ai.summarizer import Conversation_Summarizer

class Conversation_Service:

    def __init__ (
        self,
        database,
        ai_engine,
        memory_manager
    ):

        self.database = database
        self.ai_engine = ai_engine
        self.memory_manager = memory_manager

        self.summarizer = Conversation_Summarizer ()

    # ---------------------------------------------------------

    def process_message_function (
        self,
        user_message
    ):

        message = user_message.lower ().strip ()

        # -------------------------------------------------
        # Memory Recall
        # -------------------------------------------------

        recalled_value = (
            self.memory_manager
            .recall_user_information_function (
                user_message
            )
        )

        if recalled_value is not None:

            return recalled_value

        # -------------------------------------------------
        # Conversation History
        # -------------------------------------------------

        history_queries = [

            "show history",
            "conversation history",
            "recent conversation",
            "show conversation history"

        ]

        if message in history_queries:

            history = (
                self.database
                .get_recent_messages_function ()
            )

            if not history:

                return "We haven't talked yet."

            response = ""

            for speaker,text in history:

                response += (
                    f"{speaker}: {text}\n"
                )

            return response

        # -------------------------------------------------
        # Conversation Summary
        # -------------------------------------------------

        summary_queries = [

            "summary",
            "conversation summary",
            "summarize our conversation"

        ]

        if message in summary_queries:

            history = (
                self.database
                .get_recent_messages_function ()
            )

            return (
                self.summarizer
                .summarize_function (
                    history
                )
            )

        # -------------------------------------------------
        # AI ENGINE
        # -------------------------------------------------

        return (
            self.ai_engine
            .generate_response_function (
                user_message
            )
        )