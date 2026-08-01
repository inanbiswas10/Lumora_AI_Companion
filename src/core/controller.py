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
class Conversation_Controller:
    
    # Controls the overall conversation workflow of Lumora AI.

    def __init__ (self,ai_engine):

        self.ai_engine = ai_engine
        print (f"[Controller] Conversation Controller Initialized Successfully !!")
        print ()

    def start_function (self):
        
        # Start the conversation system.
      
        print (f"[Controller] Lumora AI is ready to communicate !!")
        print ()

        while True:
            user_message = input ("You: ")
            print ()
            if user_message.lower () == "exit":
                print (f"\nLumora: See you soon dear !! Please do take care of yourselfand may you have a wonderful day ahead.\n")
                break
            response = self.ai_engine.generate_response_function (user_message)
            print (f"Lumora: {response}\n")
            print ()