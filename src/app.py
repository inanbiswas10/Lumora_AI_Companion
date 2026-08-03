"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Application

Description: Responsible for initializing and coordinating all core services of Lumora AI.

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""

from src.utils.logger import Logger
from src.database.database import Database_Manager
from src.core.controller import Conversation_Controller
from src.ai.engine import AI_Engine
from src.memory.memory_manager import Memory_Manager
from src.memory.memory_extractor import Memory_Extractor
from src.memory.memory_recall import Memory_Recall
from src.services.conversation_service import Conversation_Service
from src.memory.semantic_memory import Semantic_Memory
from src.context.context_manager import Context_Manager
from src.memory.preference_manager import Preference_Manager
from src.memory.conversation_memory import Conversation_Memory
from src.memory.memory_retriever import Memory_Retriever
from src.embeddings.embedding_provider import Embedding_Provider


class Lumora_Application:
    
    # Main application class responsible for
    # creating and managing all services.

    def __init__ (self):

      self.logger = Logger ()
      self.database = Database_Manager ()
      self.ai = AI_Engine ()
      self.memory = Memory_Manager ()
      self.memory_extractor = Memory_Extractor ()
      self.memory_recall = Memory_Recall ()
      self.semantic_memory = Semantic_Memory (self.database)
      self.conversation_memory = Conversation_Memory (self.database)
      self.memory_retriever = Memory_Retriever (self.database)
      self.embedding_provider = Embedding_Provider ()
      self.conversation_service = Conversation_Service (self.database,self.ai,self.memory_extractor,self.memory_recall,self.semantic_memory,self.conversation_memory,self.memory_retriever,self.embedding_provider)
      self.controller = Conversation_Controller (self.conversation_service)
      self.preference_manager = Preference_Manager ()
      self.context_manager = Context_Manager (self.database,self.conversation_service.emotion_detector)
      
      
    def start_application_function (self):

      self.logger.info_function ("Starting Lumora AI !!")
      self.database.create_tables_function ()
      self.database.save_user_profile_function ("name","Inan")
      name = self.database.get_user_profile_function ("name")
      print (f"\n[Profile] Stored Name: {name}\n")
      print ()
      self.logger.info_function ("Lumora AI started successfully !!")
      self.controller.start_function ()

      # messages = self.database.get_all_messages_function ()

      # print (f"\n========== Conversation History ==========\n")

      # for speaker,message,timestamp in messages:

      #   print (f"[{timestamp}]")
      #   print ()
      #   print (f"{speaker} : {message}")
      #   print ()

    def shutdown_application_function (self):

      self.database.close ()
      self.logger.info_function ("Lumora AI closed successfully !!")