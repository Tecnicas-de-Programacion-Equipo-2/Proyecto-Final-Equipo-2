from tkinter import Frame, Label, Button, Entry
from CustomType.View import View
from CustomType.Passwords import Passwords, PasswordValidation

class Changepassword(Frame):

    class Constants:
        password = 'Contraseña'
        change_password = 'Cambiar contraseña'
        home = 'Home'
        add_tag = 'Agregar un tag o tarjeta'
        actual_password = 'Introduce la contraseña actual'
        tag = 'Acerca el tag o tarjeta al lector'
        bg = 'red'
        incorrect = 'Incorrecto'

        pad_backend = 10

        event = '<Button-1>'

    def __init__(self, parent, change_view_handler = None):
        super().__init__(parent)
        self.__change_view_handler = change_view_handler
        self.new_card = False
        self.label_description = Label(self, text = self.Constants.password)
        self.label_description.pack(pady = self.Constants.pad_backend, padx = self.Constants.pad_backend)

        home_button = Button(self, text = self.Constants.home,
                    command = lambda: self.__did_tap_change_button(View.Home))
        home_button.pack()

        button = Button(self, text = self.Constants.change_password)
        button.bind(self.Constants.event, self.__change_password)
        button.pack()

        button = Button(self, text = self.Constants.add_tag, command = self.__add_card)
        button.pack()

        self.__password_input = Entry(self)
        self.__password_input.pack()
        self.__password = str(self.__password_input.get())

    def __did_tap_change_button(self, view):
        if self.__change_view_handler is None:
            return
        self.__change_view_handler(view)

    def __add_card(self):
        self.label_description.configure(text = self.Constants.actual_password)
        if PasswordValidation.validation(self.__password):
            self.new_card = True
            self.label_description.configure(text = self.Constants.tag)

    def __change_password(self, event):
        self.label_description.configure(text = self.Constants.actual_password)
        if PasswordValidation.validation(self.__password):
            pass
        else:
            self.label_description.configure(bg = self.Constants.bg, text = self.Constants.incorrect)

    def new_card(self, password):
        if password !=0 and self.new_card == True:
            Passwords.new_tag(password)