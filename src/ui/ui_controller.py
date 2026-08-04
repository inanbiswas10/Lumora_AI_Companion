"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: UI Controller

Description: Acts as the bridge between the desktop interface and Lumora's backend.

Responsibilities:
    - Receive user input
    - Send messages to Conversation Service
    - Return Lumora's response
    - Keep the UI independent from backend logic

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""
class UI_Controller:

    def __init__ (self,conversation_service):
        self.conversation_service = conversation_service

    def send_message_function (self,user_message):
        response = self.conversation_service.process_message_function (user_message)
        return response

    def stream_response_function (self,user_message):
        response = self.conversation_service.process_message_function (user_message)
        for word in response.split ():
            yield word + " "
      