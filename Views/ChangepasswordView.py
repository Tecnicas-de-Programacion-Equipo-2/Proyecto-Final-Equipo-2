from tkinter import Frame, Label, Button, Entry
from CustomType.View import View
from CustomType.Passwords import Passwords, PasswordValidation

class Changepassword(Frame):

    class Constants:
        event = '<Button-1>'


    def __init__(self, parent, change_view_handler = None):
        super().__init__(parent)
        self.__change_view_handler = change_view_handler
        self.new_card = False
        self.label_description = Label(self, text = "Password")
        self.label_description.pack(pady = 10, padx = 10)

        home_button = Button(self, text="Home",
                    command=lambda: self.__did_tap_change_button(View.Home))
        home_button.pack()

        button = Button(self, text="Change password")
        button.bind(self.Constants.event, self.__change_password)
        button.pack()

        button = Button(self, text="Add tag or card", command=self.__add_card)
        button.pack()

        self.__password_input = Entry(self)
        self.__password_input.pack()
        self.__password = str(self.__password_input.get())


    def __did_tap_change_button(self, view):
        if self.__change_view_handler is None:
            return
        self.__change_view_handler(view)

    def __add_card(self):
        self.label_description.configure(text="Introduce the actual password")
        if PasswordValidation.validation(self.__password):
            self.new_card = True
            self.label_description.configure(text="Near the tag or card to the lector")

    def __change_password(self, event):
        self.label_description.configure(text="Introduce the actual password")
        if PasswordValidation.validation(self.__password):
            pass
        else:
            self.label_description.configure(bg = "red", text="Incorrect")

    def new_card(self, password):
        if password !=0 and self.new_card == True:
            Passwords.new_tag(password)