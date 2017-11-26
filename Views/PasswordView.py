from tkinter import Frame, Label, Button, Entry, N, S, E, W
from CustomType.View import View

class PasswordView(Frame):
    class Constants:
        title = "Login"
        login = "Enter"
        password_label = "Password"
        separator_text = "▶"
        event = '<Return>'
        center = N, S, E, W
        title_label =150
        separator_width = 50
        validation = "Incorrect password"
        password = '12345'


    def __init__(self, parent, change_view_handler = None):
        super().__init__(parent)

        self.__change_view_handler = change_view_handler
        self.grid_rowconfigure(0, minsize=125)
        self.grid_columnconfigure(0, minsize=self.Constants.title_label)
        self.grid_columnconfigure(2, minsize=self.Constants.title_label)
        self.grid_columnconfigure(1, minsize=self.Constants.separator_width)




