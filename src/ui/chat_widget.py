"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Chat Widget

Description: Represents a single chat bubble inside the conversation.

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""

from PySide6.QtWidgets import (QWidget,QLabel,QHBoxLayout,QFrame
)

from PySide6.QtCore import Qt


class Chat_Widget (QWidget):

    def __init__ (self,message,is_user = False):

        super ().__init__ ()

        self.message = message
        self.is_user = is_user

        self.build_ui_function ()

    def build_ui_function (self):

        outer_layout = QHBoxLayout ()

        bubble = QFrame ()

        if self.is_user:
            bubble.setObjectName ("userBubble")
        else:
            bubble.setObjectName ("lumoraBubble")

        bubble_layout = QHBoxLayout ()

        label = QLabel (self.message)

        label.setWordWrap (True)

        bubble_layout.addWidget (label)

        bubble.setLayout (bubble_layout)

        if self.is_user:

            outer_layout.addStretch ()

            outer_layout.addWidget (bubble)

        else:

            outer_layout.addWidget (bubble)

            outer_layout.addStretch ()

        self.setLayout (outer_layout)