"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: AI Engine

Description: Central intelligence module of Lumora AI.

Responsibilities:
    - Update memory
    - Build conversation context
    - Generate prompts
    - Call the language model
    - Format responses
    - Save conversations

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""

from src.context.context_manager import Context_Manager

class AI_Engine:

    def __init__ (
        self,
        database,
        memory_manager,
        emotion_detector,
        prompt_builder,
        llm_provider,
        response_formatter
    ):

        self.database = database
        self.memory_manager = memory_manager

        self.context_manager = Context_Manager (
            database,
            memory_manager,
            emotion_detector
        )

        self.prompt_builder = prompt_builder
        self.llm_provider = llm_provider
        self.response_formatter = response_formatter

    # ---------------------------------------------------------

    def generate_response_function (self,user_message):

        # ------------------------------------------
        # Save user message
        # ------------------------------------------

        self.database.save_message_function (
            "User",
            user_message
        )

        # ------------------------------------------
        # Update memory
        # ------------------------------------------

        self.memory_manager.process_user_message_function (
            user_message
        )

        # ------------------------------------------
        # Build context
        # ------------------------------------------

        context = (
            self.context_manager
            .build_context_function (
                user_message
            )
        )

        # ------------------------------------------
        # Build prompt
        # ------------------------------------------

        prompt = (
            self.prompt_builder
            .build_prompt_function (
                user_message,
                context
            )
        )

        # ------------------------------------------
        # Generate response
        # ------------------------------------------

        response = (
            self.llm_provider
            .generate_response_function (
                prompt
            )
        )

        # ------------------------------------------
        # Format response
        # ------------------------------------------

        response = (
            self.response_formatter
            .format_response_function (
                response
            )
        )

        # ------------------------------------------
        # Save Lumora response
        # ------------------------------------------

        self.database.save_message_function (
            "Lumora",
            response
        )
        return response