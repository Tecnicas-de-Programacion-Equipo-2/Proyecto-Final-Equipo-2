from tkinter import Frame, Label, Button, Entry
from CustomType.View import View
from CustomType.Passwords import ChangePasswords

class Changepassword(Frame):

    class Constants:
        change_password = 'Modificar contraseña'
        password_changed = 'Contraseña modificada'
        home = 'Home'
        add_tag = 'Agregar un tag o tarjeta'
        actual_password = 'Introduce la contraseña actual y presiona la accion'
        tag = 'Acerca el tag o tarjeta al lector'
        bg = 'red'
        incorrect = 'Contraseña incorrecta'
        caracter = '*'
        color1 = 'lightblue'
        new_password = 'Introduce la nueva contraseña y presiona enter'
        color2 = 'lightslategray'
        enter = 'Enter'
        new_tag = 'New tag added'

        pad_backend = 10

    def __init__(self, parent, change_view_handler = None):
        super().__init__(parent)
        self.__change_view_handler = change_view_handler
        self.__add = False
        self.__confirmation = False
        self.label_description = Label(self, text = self.Constants.actual_password)
        self.label_description.pack(pady = self.Constants.pad_backend, padx = self.Constants.pad_backend)

        home_button = Button(self, text = self.Constants.home,
                    command = lambda: self.__did_tap_change_button(View.Home))
        home_button.pack()

        self.__password_input = Entry(self, show = self.Constants.caracter)
        self.__password_input.pack()

        button = Button(self, text = self.Constants.change_password, command = self.__change_password)
        button.pack()

        button = Button(self, text = self.Constants.add_tag, command = self.__add_card)
        button.pack()

    def __did_tap_change_button(self, view):
        if self.__change_view_handler is None:
            return
        self.label_description.configure(text = self.Constants.actual_password)
        if self.__confirmation:
            self.__enter_button.destroy()
            self.__confirmation = False
        self.__change_view_handler(view)

    def __add_card(self):
        password = str(self.__password_input.get())
        if ChangePasswords.validation(password):
            self.__add = True
            self.label_description.configure(bg = self.Constants.color1, text = self.Constants.tag)
        else:
            self.label_description.configure(bg = self.Constants.bg, text = self.Constants.incorrect)
            self.__password_input.delete(0, 'end')

    def __change_password(self):
        password = str(self.__password_input.get())
        if ChangePasswords.validation(password):
            self.label_description.configure(bg = self.Constants.color1, text = self.Constants.new_password)
            self.__password_input.delete(0, 'end')
            if self.__confirmation == False:
                self.__enter_button = Button(self, bg = self.Constants.color2, text = self.Constants.enter,
                                             command = self.__send_password)
                self.__enter_button.pack()
            self.__confirmation = True
        else:
            self.label_description.configure(bg = self.Constants.bg, text = self.Constants.incorrect)
            self.__password_input.delete(0, 'end')

    def new_card(self, password):
        if self.__add == True:
            new = {
                'type': 'card',
                'password': password
            }
            ChangePasswords.new_card(new)
            self.label_description.configure(bg=self.Constants.color1, text = self.Constants.new_tag)
            self.__add = False

    def __send_password(self):
        if self.__confirmation:
            new_password = str(self.__password_input.get())
            ChangePasswords.change_passwords(new_password)
            self.__password_input.delete(0, 'end')
            self.label_description.configure(bg = self.Constants.color1, text = self.Constants.password_changed)