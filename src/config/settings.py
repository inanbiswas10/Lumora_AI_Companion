"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Settings

Description: Stores all global configuration values used throughout Lumora AI.

Responsibilities:
    - Application settings
    - AI model settings
    - Memory settings
    - Database settings

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""


class Settings:

    # ---------------------------------------------------
    # Application
    # ---------------------------------------------------

    APP_NAME = "Lumora AI"

    TAGLINE = "Conversations that Care. Technology that Understands."

    VERSION = "0.1.0-alpha"

    AUTHOR = "Inan Biswas"

    # ---------------------------------------------------
    # Database
    # ---------------------------------------------------

    DATABASE_NAME = "lumora.db"

    # ---------------------------------------------------
    # Large Language Model
    # ---------------------------------------------------

    LLM_MODEL = "llama-3.3-70b-versatile"

    # ---------------------------------------------------
    # Embedding Model
    # ---------------------------------------------------

    EMBEDDING_MODEL = "all-MiniLM-L6-v2"

    # ---------------------------------------------------
    # Memory
    # ---------------------------------------------------

    MEMORY_TOP_K = 3

    MEMORY_SIMILARITY_THRESHOLD = 0.75

    MAX_CONVERSATION_HISTORY = 10