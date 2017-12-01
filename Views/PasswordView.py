from tkinter import Frame, Label, Button, Entry, N, S, E, W
from CustomType.View import View
from CustomType.Passwords import ChangePasswords

class PasswordView(Frame):

    class Constants:
        title = 'Login'
        login = 'Enter'
        password_label = 'Contraseña'
        separator_text = '▶'
        event = '<Return>'
        validation = 'Contraseña Incorrecta'
        bg_button = 'lightslategray'
        bg_validation = 'red'
        caracter = '*'

        title_label = 150
        separator_width = 50

        center = N, S, E, W

    def __init__(self, parent, change_view_handler = None, open_door = None):
        super().__init__(parent)

        ChangePasswords.validation(45)

        self.__change_view_handler = change_view_handler
        self.__open_door = open_door

        self.__configure_grid()

        self.__configure_UI()

    def __configure_grid(self):
        self.grid_rowconfigure(0, minsize = 125)
        self.grid_columnconfigure(0, minsize = self.Constants.title_label)
        self.grid_columnconfigure(2, minsize = self.Constants.title_label)
        self.grid_columnconfigure(1, minsize = self.Constants.separator_width)

    def __configure_UI(self):
        self.__title_label = Label(self, text = self.Constants.title)
        self.__title_label.grid(row = 0, column = 1, sticky = self.Constants.center)
        self.__separator_label = Label(self, text = self.Constants.separator_text)
        self.__separator_label.grid(row = 1, column = 1, sticky = self.Constants.center)
        self.__password_label = Label(self, text = self.Constants.password_label)
        self.__password_label.grid(row = 1, column = 0, sticky = self.Constants.center)

        self.__password_input = Entry(self, show = self.Constants.caracter)
        self.__password_input.grid(row = 1, column = 2, sticky = self.Constants.center)

        self.__enter_button = Button(self)
        self.__enter_button.configure(bg = self.Constants.bg_button, text = self.Constants.login,
                                      command = lambda: self.__did_tap_change_button(View.Home))
        self.__enter_button.grid(row = 2, column = 0, columnspan = 3, sticky = self.Constants.center)

        self.__validation_label = Label(self)
        self.__validation_label.grid(row = 3, column = 0, columnspan = 3, sticky = self.Constants.center)

    def __did_tap_change_button(self, view):
        password = str(self.__password_input.get())
        if self.__change_view_handler is None:
            return
        elif ChangePasswords.validation(password):
            self.__change_view_handler(view)
        else:
            self.__validation_label.configure(text = self.Constants.validation, bg = self.Constants.bg_validation)

    def try_card(self, password):
        if ChangePasswords.validation(password):
            self.__change_view_handler(View.Home)
            self.__open_door("DoorO")
        else: return