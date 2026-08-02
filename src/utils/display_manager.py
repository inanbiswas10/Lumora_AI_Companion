"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Display Manager

Description: Handles all terminal output shown to the user.

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""

class Display_Manager:

    @staticmethod
    def user_message (message):

        print ()
        print ("You:")
        print ()
        print (message)
        print ()


    @staticmethod
    def ai_message (message):

        print ()
        print ("Lumora:")
        print ()
        print (message)
        print ()


    @staticmethod
    def system_message (message):

        print ()
        print (message)
        print ()