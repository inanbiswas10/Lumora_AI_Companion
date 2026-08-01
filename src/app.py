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


class Lumora_Application:
    
    # Main application class responsible for
    # creating and managing all services.

    def __init__ (self):

      self.logger = Logger ()
      self.database = Database_Manager ()
      self.ai = AI_Engine ()
      self.controller = Conversation_Controller (self.ai,self.database,self.logger)

    def start_application_function (self):

      self.logger.info_function ("Starting Lumora AI !!")
      self.database.create_tables_function ()
      messages = self.database.get_all_messages_function ()

      print (f"\n========== Conversation History ==========\n")

      for speaker,message,timestamp in messages:

        print (f"[{timestamp}]")
        print ()
        print (f"{speaker} : {message}")
        print()

      self.logger.info_function ("Lumora AI started successfully !!")
      self.controller.start_function ()

    def shutdown_application_function (self):

      self.database.close ()
      self.logger.info_function ("Lumora AI closed successfully !!")