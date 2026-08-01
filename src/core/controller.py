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

    def __init__ (self,ai_engine,database,logger):

        self.ai_engine = ai_engine
        self.database = database
        self.logger = logger
        print (f"[Controller] Conversation Controller Initialized Successfully !!")
        print ()

    def start_function (self):
        
        # Start the conversation system.
      
        print (f"[Controller] Lumora AI is ready to communicate !!")
        print ()
        print (f"Type 'exit' to close Lumora AI.\n")

        while True:
            user_message = input ("You: ")
            print ()
            if user_message.lower () == "exit":
                print (f"\nLumora: See you soon dear !! Please do take care of yourself and may you have a wonderful day ahead.\n")
                break

            # Save the user's message
            self.database.save_message_function ("User",user_message)

            # Generate AI response   
            response = self.ai_engine.generate_response_function (user_message)

            # Save Lumora's response
            self.database.save_message_function ("Lumora",response)

            # Display the response
            print (f"Lumora: {response}\n")
            print ()