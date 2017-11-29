from tkinter import Frame, Label, Button, Entry
from CustomType.View import View
from CustomType.Passwords import ChargePasswords

class Changepassword(Frame):

    class Constants:
        event = '<Button-1>'

    def __init__(self, parent, change_view_handler = None):
        super().__init__(parent)
        self.__change_view_handler = change_view_handler
        self.__add = False
        self.__confirmation = False
        self.label_description = Label(self, text = "Introduce the actual password and click an action")
        self.label_description.pack(pady = 10, padx = 10)

        home_button = Button(self, text="Home",
                    command=lambda: self.__did_tap_change_button(View.Home))
        home_button.pack()

        self.__password_input = Entry(self, show='*')
        self.__password_input.pack()

        button = Button(self, text="Change password", command=self.__change_password)
        button.pack()

        button = Button(self, text="Add tag or card", command=self.__add_card)
        button.pack()

    def __did_tap_change_button(self, view):
        if self.__change_view_handler is None:
            return
        self.label_description.configure(text="Introduce the actual password and click an action")
        self.__enter_button.destroy()
        self.__change_view_handler(view)

    def __add_card(self):
        password = int(self.__password_input.get())
        if ChargePasswords.validation(password):
            self.__add = True
            self.label_description.configure(bg = "lightblue", text="Near the tag or card to the lector")
        else:
            self.label_description.configure(bg = "red", text="Incorrect password")
            self.__password_input.delete(0, 'end')

    def __change_password(self):
        password = str(self.__password_input.get())
        if ChargePasswords.validation(password):
            self.label_description.configure(bg = "lightblue", text="Introduce the new password and press enter")
            self.__password_input.delete(0, 'end')
            if self.__confirmation == False:
                self.__enter_button = Button(self, bg="lightslategray", text="Enter")
                self.__enter_button.bind(self.Constants.event, self.__send_password)
                self.__enter_button.pack()
            self.__confirmation = True
        else:
            self.label_description.configure(bg = "red", text="Incorrect password")
            self.__password_input.delete(0, 'end')

    def new_card(self, password):
        if self.__add == True:
            new={
                "type": "card",
                "password": password
            }
            ChargePasswords.new_card(new)
            self.__add = False

    def __send_password(self, event):
        if self.__confirmation:
            new_password = str(self.__password_input.get())
            ChargePasswords.change_passwords(new_password)
            self.__password_input.delete(0, 'end')
            self.label_description.configure(bg="lightblue", text="Password changed")
            self.__confirmation = False