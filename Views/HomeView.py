from tkinter import Frame, Label, Button
from CustomType.View import View

class HomeView(Frame):

    def __init__(self, parent, change_view_handler = None):
        super().__init__(parent)

        self.__change_view_handler = change_view_handler

        label = Label(self, text = "Home")
        label.pack(pady = 10, padx = 10)

        button = Button(self, text = "Habitacion 1",
                        command = lambda: self.__did_tap_change_button(View.Room1))
        button.pack()
        button = Button(self, text = "Habitacion 2",
                        command = lambda: self.__did_tap_change_button(View.Room2))
        button.pack()
        button = Button(self, text = "Habitacion 3",
                        command = lambda: self.__did_tap_change_button(View.Room3))
        button.pack()
        button = Button(self, text="Habitacion 4",
                        command = lambda: self.__did_tap_change_button(View.Room4))
        button.pack()

        change_password_button = Button(self, text="Change password or add tag",
                    command=lambda: self.__did_tap_change_button(View.Changepassword))
        change_password_button.pack()

    def __did_tap_change_button(self, view):
        if self.__change_view_handler is None:
            return
        self.__change_view_handler(view)