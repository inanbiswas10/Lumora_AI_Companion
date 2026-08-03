"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Message Input

Description: Bottom input area where the user types messages and sends them to Lumora.

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""

from PySide6.QtWidgets import (QWidget,QHBoxLayout,QLineEdit,QPushButton,)

class Message_Input (QWidget):

    def __init__ (self):

        super ().__init__ ()

        self.build_ui_function ()

    def build_ui_function (self):

        layout = QHBoxLayout ()

        # -----------------------------
        # Message Textbox
        # -----------------------------

        self.input_box = QLineEdit ()

        self.input_box.setPlaceholderText(
            "Type your message !!"
        )

        # Press Enter to send
        self.input_box.returnPressed.connect (
            self.send_button_clicked_function
        )

        # -----------------------------
        # Send Button
        # -----------------------------

        self.send_button = QPushButton ("➤")

        self.send_button.setObjectName ("sendButton")

        self.send_button.setFixedWidth (70)

        self.send_button.setFixedHeight (50)

        # -----------------------------
        # Layout
        # -----------------------------

        layout.addWidget (self.input_box)

        layout.addWidget (self.send_button)

        self.setLayout (layout)

    # ==========================================================
    # Returns the user message
    # ==========================================================

    def get_text_function (self):

        return self.input_box.text ()

    # ==========================================================
    # Clears the input field
    # ==========================================================

    def clear_function (self):

        self.input_box.clear ()

    # ==========================================================
    # Trigger send button when Enter is pressed
    # ==========================================================

    def send_button_clicked_function (self):

        self.send_button.click ()