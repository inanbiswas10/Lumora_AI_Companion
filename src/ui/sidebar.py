from PySide6.QtWidgets import (QWidget,QVBoxLayout,QLabel,QPushButton)

from PySide6.QtCore import Qt


class Sidebar (QWidget):

    def __init__ (self):

        super ().__init__ ()
        self.setObjectName ("sidebar")
        self.build_ui_function ()

    def build_ui_function (self):

        layout = QVBoxLayout ()

        self.title = QLabel ("✨ Lumora AI")

        self.title.setAlignment (Qt.AlignCenter)

        self.subtitle = QLabel ("Conversations that Care.\n"
                                "Technology that Understands."
        )
        self.subtitle.setAlignment (Qt.AlignCenter)

        self.title.setObjectName ("title")

        self.subtitle.setObjectName ("subtitle")

        self.new_chat_button = QPushButton ("➕  New Chat")

        self.history_button = QPushButton ("💬  Chat History")

        self.memory_button = QPushButton ("🧠  Memories")

        self.profile_button = QPushButton ("👤  Profile")

        self.settings_button = QPushButton ("⚙  Settings")

        layout.addWidget (self.title)

        layout.addWidget (self.subtitle)

        layout.addSpacing (25)

        layout.addWidget (self.new_chat_button)

        layout.addWidget (self.history_button)

        layout.addWidget (self.memory_button)

        layout.addWidget (self.profile_button)

        layout.addWidget (self.settings_button)

        layout.addStretch ()

        self.footer = QLabel ("Lumora AI v1.0")

        self.footer.setAlignment (Qt.AlignCenter)

        layout.addWidget (self.footer)

        self.setLayout (layout)

        self.setFixedWidth (260)