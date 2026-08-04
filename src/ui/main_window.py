from PySide6.QtWidgets import (QMainWindow,QWidget,QHBoxLayout,QVBoxLayout)
from src.ui.sidebar import Sidebar
from src.ui.chat_area import Chat_Area
from src.ui.avatar_panel import Avatar_Panel
from src.ui.message_input import Message_Input
from PySide6.QtCore import QTimer
import random

class Main_Window (QMainWindow):

    def __init__ (self,ui_controller):

        super ().__init__()
        self.ui_controller = ui_controller
        self.setWindowTitle ("Lumora AI Companion •")
        self.resize (1450,900)
        self.build_ui_function ()
        self.stream_timer = QTimer ()
        self.stream_timer.timeout.connect (self.stream_next_word_function)
        self.stream_words = []
        self.stream_index = 0

    def send_message_function (self):

        user_message = self.message_input.get_text_function ()

        if not user_message.strip ():
            return

        # Display the user's message
        self.chat_area.add_user_message (user_message)

        # Clear the input field
        self.message_input.clear_function ()

        # Show the typing indicator
        self.chat_area.show_typing_indicator_function ()

        # Get Lumora's response
        response = self.ui_controller.send_message_function (user_message)

        # Prepare the response for streaming
        self.stream_words = response.split ()

        self.stream_index = 0

        # Calculate a human-like thinking time
        response_length = len (response)

        thinking_time = max (1200,min (3000,response_length*18))

        # Start streaming after the thinking delay
        QTimer.singleShot (thinking_time,lambda: self.stream_timer.start (90))

    def stream_next_word_function (self):

        if self.stream_index == 0:

           self.chat_area.hide_typing_indicator_function ()

           self.chat_area.create_empty_lumora_message_function ()

        if self.stream_index >= len (self.stream_words):

            self.stream_timer.stop ()

            self.chat_area.finish_stream_function ()

            return

        word = self.stream_words [self.stream_index]

        self.chat_area.append_stream_text_function (word + " ")

        self.stream_index += 1

        if word.endswith ("."):
            self.stream_timer.setInterval (300)

        elif word.endswith ("?"):
            self.stream_timer.setInterval (350)

        elif word.endswith ("!"):
            self.stream_timer.setInterval (320)

        elif word.endswith (","):
            self.stream_timer.setInterval (180)

        else:
            self.stream_timer.setInterval (90)

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