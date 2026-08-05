"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Application

Description: Initializes and coordinates all core components of Lumora AI.

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""

from PySide6.QtWidgets import QApplication
from src.utils.logger import Logger
from src.database.database import Database_Manager

# Memory
from src.memory.memory_extractor import Memory_Extractor
from src.memory.memory_recall import Memory_Recall
from src.memory.semantic_memory import Semantic_Memory
from src.memory.conversation_memory import Conversation_Memory
from src.memory.memory_retriever import Memory_Retriever
from src.memory.semantic_retriever import Semantic_Retriever
from src.memory.importance_analyzer import Importance_Analyzer
from src.memory.memory_manager import Memory_Manager

# Embeddings
from src.embeddings.embedding_provider import Embedding_Provider

# AI
from src.ai.engine import AI_Engine
from src.ai.emotion_detector import Emotion_Detector
from src.ai.personality_engine import Personality_Engine

# Prompt
from src.prompt.prompt_builder import Prompt_Builder

# LLM
from src.llm.groq_provider import Groq_Provider

# Utils
from src.utils.response_formatter import Response_Formatter

# Services
from src.services.conversation_service import Conversation_Service

# Controller
from src.core.controller import Conversation_Controller

# UI
from src.ui.ui_controller import UI_Controller
from src.ui.main_window import Main_Window
from src.ui.theme import LUMORA_THEME


class Lumora_Application:

    def __init__ (self):

        # -------------------------------------------------
        # Logger
        # -------------------------------------------------

        self.logger = Logger ()

        # -------------------------------------------------
        # Database
        # -------------------------------------------------

        self.database = Database_Manager ()

        # -------------------------------------------------
        # Memory Components
        # -------------------------------------------------

        self.memory_extractor = Memory_Extractor ()

        self.memory_recall = Memory_Recall (self.database)

        self.semantic_memory = Semantic_Memory (
            self.database
        )

        self.conversation_memory = Conversation_Memory (
            self.database
        )

        self.memory_retriever = Memory_Retriever (
            self.database
        )

        self.embedding_provider = Embedding_Provider ()

        self.importance_analyzer = Importance_Analyzer ()

        self.semantic_retriever = Semantic_Retriever (
            self.database,
            self.embedding_provider
        )

        self.memory_manager = Memory_Manager (
            self.database,
            self.memory_extractor,
            self.memory_recall,
            self.semantic_memory,
            self.conversation_memory,
            self.semantic_retriever,
            self.importance_analyzer
        )

        # -------------------------------------------------
        # AI Components
        # -------------------------------------------------

        self.emotion_detector = Emotion_Detector ()

        self.personality_engine = Personality_Engine ()

        self.prompt_builder = Prompt_Builder (
            self.personality_engine
        )

        self.llm_provider = Groq_Provider ()

        self.response_formatter = Response_Formatter ()

        self.ai_engine = AI_Engine (
            self.database,
            self.memory_manager,
            self.emotion_detector,
            self.prompt_builder,
            self.llm_provider,
            self.response_formatter
        )

        # -------------------------------------------------
        # Services
        # -------------------------------------------------

        self.conversation_service = Conversation_Service (
            self.database,
            self.ai_engine,
            self.memory_manager
        )

        # -------------------------------------------------
        # Controllers
        # -------------------------------------------------

        self.ui_controller = UI_Controller (
            self.conversation_service
        )

        self.controller = Conversation_Controller (
            self.conversation_service
        )

    # =====================================================

    def start_application_function (self):

        self.logger.info_function (
            "Starting Lumora AI..."
        )

        self.database.create_tables_function()

        app = QApplication ([])

        app.setStyleSheet (LUMORA_THEME)

        window = Main_Window (
            self.ui_controller
        )

        window.show ()

        app.exec ()

    # =====================================================

    def shutdown_application_function (self):

        self.database.close ()

        self.logger.info_function (
            "Lumora AI closed successfully."
        )