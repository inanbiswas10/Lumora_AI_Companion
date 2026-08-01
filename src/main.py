"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Project Entry Point

Description: This is the main entry point of the Lumora AI application. It initializes the system and co-ordinates the startup process.

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""

from src.core.controller import Conversation_Controller

def display_banner_function ():
    # Display the Lumora AI startup banner.
    
    print ()
    print ("="*60)
    print (f"                  Welcome to Lumora AI")
    print ()
    print (f"Conversations that Care. Technology that Understands.")
    print ("="*60)
    print ()


def main_function ():
    # Main entry point of the application.

    display_banner_function ()
    controller = Conversation_Controller ()
    controller.start_function ()

if __name__ == "__main__":
    main_function ()