"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Avatar Panel

Description: Displays Lumora's identity, avatar, and current status.

Responsibilities:
    - Display Lumora's avatar
    - Show online/offline status
    - Display AI information
    - Reserved space for future animations

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""

from PySide6.QtWidgets import (QWidget,QLabel,QVBoxLayout,QFrame)

from PySide6.QtCore import Qt


class Avatar_Panel (QWidget):

    # Displays Lumora's avatar and status.

    def __init__ (self):

        super ().__init__ ()

        self.setObjectName ("avatarPanel")

        self.build_ui_function ()

    def build_ui_function (self):

        layout = QVBoxLayout ()

        # ==========================================================
        # Title
        # ==========================================================

        self.title = QLabel ("Lumora")

        self.title.setAlignment (Qt.AlignCenter)

        # ==========================================================
        # Subtitle
        # ==========================================================

        self.subtitle = QLabel (
            "Artificial Intelligence Companion"
        )

        self.subtitle.setAlignment (Qt.AlignCenter)

        # ==========================================================
        # Avatar Placeholder
        # ==========================================================

        self.avatar = QLabel ("🤖")

        self.avatar.setAlignment (Qt.AlignCenter)

        self.avatar.setFixedSize (180,180)

        # ==========================================================
        # Status
        # ==========================================================

        self.status = QLabel ("🟢 Online")

        self.status.setAlignment (Qt.AlignCenter)

        # ==========================================================
        # Information
        # ==========================================================

        self.info = QLabel (
            "Always learning.\nAlways listening."
        )

        self.info.setAlignment (Qt.AlignCenter)

        # ==========================================================
        # Assemble Layout
        # ==========================================================

        layout.addWidget (self.title)

        layout.addWidget (self.subtitle)

        layout.addStretch ()

        layout.addWidget (self.avatar)

        layout.addWidget (self.status)

        layout.addWidget (self.info)

        layout.addStretch ()

        self.setLayout (layout)

        self.setFixedWidth (300)