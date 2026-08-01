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

from src.config.settings import Settings
from src.app import Lumora_Application

def display_banner_function ():
    # Display the Lumora AI startup banner.
    
    print ()
    print ("="*60)
    print (f"                  Welcome to {Settings.APP_NAME} !!")
    print ()
    print (f"{Settings.TAGLINE}")
    print ("="*60)
    print ()


def main_function ():
    # Main entry point of the application.

    display_banner_function ()
    application = Lumora_Application ()
    application.start_application_function ()
    application.shutdown_application_function ()

if __name__ == "__main__":
    main_function ()