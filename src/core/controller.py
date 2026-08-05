"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Conversation Controller

Description: This module acts as the central co-ordinator of Lumora AI.

Responsibilities:
    - Coordinate all modules
    - Manage conversation workflow
    - Route requests between components
    - Handle application lifecycle

Author: Inan Biswas
Project: Lumora AI
=========================================================================

"""
from src.utils.display_manager import Display_Manager

class Conversation_Controller:
    
    # Controls the overall conversation workflow of Lumora AI.

    def __init__ (self,conversation_service):
        self.conversation_service = conversation_service

        print (f"Conversation Controller Initialized Successfully !!")
        print ()

    def start_function (self):
        
        # Start the conversation system.
      
        print (f"Lumora AI is ready to communicate !!")
        print ()
        print (f"Type 'exit' to close Lumora AI.\n")

        friendly_labels = {
        
            "name":"your name",
            "favorite_colour":"your favourite colour",
            "university":"your university",
            "workplace":"your workplace",
            "hobby":"your hobby",
            "interest":"your interest"
        }
        while True:
            print ()
            user_message = input ("You: ")
            print ()

            if user_message.lower () == "exit":
                print (f"Lumora: See you soon dear !! Please take care of yourself and may you have a wonderful day ahead.")
                print ()
                break
            response = self.conversation_service.process_message_function (user_message)

            print ()
            Display_Manager.ai_message (response)
            print ()