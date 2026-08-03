from PySide6.QtWidgets import (QMainWindow,QWidget,QHBoxLayout,QVBoxLayout)

from src.ui.sidebar import Sidebar
from src.ui.chat_area import Chat_Area
from src.ui.avatar_panel import Avatar_Panel
from src.ui.message_input import Message_Input

class Main_Window (QMainWindow):
    def __init__ (self,ui_controller):

        super ().__init__()
        self.ui_controller = ui_controller
        self.setWindowTitle ("Lumora AI Companion •")
        self.resize (1450,900)
        self.build_ui_function ()

    def send_message_function (self):
        user_message = self.message_input.get_text_function ()
        if not user_message.strip ():
            return
        self.chat_area.add_user_message (user_message)
        response = self.ui_controller.send_message_function (user_message)
        self.chat_area.add_lumora_message (response)
        self.message_input.clear_function ()

    def build_ui_function (self):
        central_widget = QWidget ()

        self.setCentralWidget (central_widget)

        main_layout = QVBoxLayout ()

        content_layout = QHBoxLayout ()

        self.sidebar = Sidebar ()

        self.chat_area = Chat_Area ()

        self.avatar_panel = Avatar_Panel ()

        self.message_input = Message_Input ()

        content_layout.addWidget (self.sidebar)

        content_layout.addWidget (self.chat_area,3)

        content_layout.addWidget (self.avatar_panel)

        main_layout.addLayout (content_layout)

        main_layout.addWidget (self.message_input)

        self.message_input.send_button.clicked.connect (self.send_message_function)

        central_widget.setLayout (main_layout)