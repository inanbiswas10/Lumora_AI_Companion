from PySide6.QtWidgets import (QWidget,QVBoxLayout,QLabel,QScrollArea,QFrame)
from PySide6.QtCore import Qt,QTimer
from src.ui.chat_widget import Chat_Widget

class Chat_Area (QWidget):

    def __init__ (self):

        super ().__init__ ()

        self.current_lumora_widget = None

        self.typing_timer = QTimer ()

        self.typing_timer.timeout.connect (self.animate_typing_indicator_function)

        self.typing_state = 0

        self.typing_label = None

        self.typing_label = None

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

        self.chat_layout.insertWidget (self.chat_layout.count ()-1,bubble)

    def add_lumora_message (self,message):

        bubble = Chat_Widget (message,False)

        self.chat_layout.insertWidget (self.chat_layout.count ()-1,bubble)

    def create_empty_lumora_message_function (self):

        self.current_lumora_widget = Chat_Widget("", False)

        self.chat_layout.insertWidget (self.chat_layout.count()-1,self.current_lumora_widget)

        return self.current_lumora_widget

    def append_stream_text_function (self,text):

        if self.current_lumora_widget:

            current = self.current_lumora_widget.message_label.text ()

            self.current_lumora_widget.set_message_function (current + text)

            scrollbar = self.scroll_area.verticalScrollBar ()

            scrollbar.setValue (scrollbar.maximum ())

    def show_typing_indicator_function (self):

        self.typing_label = QLabel ("Lumora is typing.")

        self.typing_label.setObjectName ("typingIndicator")

        self.chat_layout.insertWidget (self.chat_layout.count ()-1,self.typing_label)

        self.typing_state = 0

        self.typing_timer.start (400)

        scrollbar = self.scroll_area.verticalScrollBar ()

        scrollbar.setValue (scrollbar.maximum ())

    def animate_typing_indicator_function (self):

        if self.typing_label is None:
           return

        dots = "."*((self.typing_state % 3) + 1)

        self.typing_label.setText (f"Lumora is typing{dots}")

        self.typing_state += 1

    def hide_typing_indicator_function (self):

        if self.typing_label is None:
           return

        self.typing_timer.stop ()

        self.chat_layout.removeWidget (self.typing_label)

        self.typing_label.deleteLater ()

        self.typing_label = None

    def finish_stream_function (self):

        self.current_lumora_widget = None