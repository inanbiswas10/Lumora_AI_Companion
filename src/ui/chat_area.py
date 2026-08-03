from PySide6.QtWidgets import (QWidget,QVBoxLayout,QScrollArea)

from src.ui.chat_widget import Chat_Widget


class Chat_Area (QWidget):

    def __init__ (self):

        super ().__init__ ()

        self.build_ui_function ()

    def build_ui_function (self):

        main_layout = QVBoxLayout ()

        self.scroll_area = QScrollArea ()

        self.scroll_area.setWidgetResizable (True)

        self.container = QWidget ()

        self.chat_layout = QVBoxLayout ()

        self.chat_layout.addStretch ()

        self.container.setLayout (self.chat_layout)

        self.scroll_area.setWidget (self.container)

        main_layout.addWidget (self.scroll_area)

        self.setLayout (main_layout)

    def add_user_message (self,message):

        bubble = Chat_Widget (message,True)

        self.chat_layout.insertWidget (
            self.chat_layout.count ()-1,
            bubble
        )

    def add_lumora_message (self,message):

        bubble = Chat_Widget (message,False)

        self.chat_layout.insertWidget (
            self.chat_layout.count ()-1,
            bubble
        )