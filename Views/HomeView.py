from tkinter import Frame, Label, Button
from CustomType.Functions import Functions
from CustomType.View import View

class HomeView(Frame):

    class Constants:
        home = 'Home'
        room_1 = 'Habitacion 1'
        room_2 = 'Habitacion 2'
        room_3 = 'Habitacion 3'
        room_4 = 'Habitacion 4'
        change = 'Change password or add tag'
        fg = '#d80808'
        alert_text = 'FIRE DETECTED'
        no_fire = ''

        pad_backend = 10

    def __init__(self, parent, change_view_handler = None):
        super().__init__(parent)

        self.__change_view_handler = change_view_handler

        self.__configure_home_UI()

        self.__functions = {
            Functions.FireAlert: self.__fire_alert,
            Functions.CeaseFireAlert: self.__cease_fire_alert
        }

    def __configure_home_UI(self):
        label = Label(self, text = self.Constants.home)
        label.pack(pady = self.Constants.pad_backend, padx = self.Constants.pad_backend)

        self.__alert_fire = Label(self, text = self.Constants.no_fire)
        self.__alert_fire.pack(padx = self.Constants.pad_backend, pady = self.Constants.pad_backend)

        button = Button(self, text = self.Constants.room_1,
                        command = lambda: self.__did_tap_change_button(View.Room1))
        button.pack()
        button = Button(self, text = self.Constants.room_2,
                        command = lambda: self.__did_tap_change_button(View.Room2))
        button.pack()
        button = Button(self, text = self.Constants.room_3,
                        command = lambda: self.__did_tap_change_button(View.Room3))
        button.pack()
        button = Button(self, text = self.Constants.room_4,
                        command = lambda: self.__did_tap_change_button(View.Room4))
        button.pack()

        change_password_button = Button(self, text = self.Constants.change,
                    command = lambda: self.__did_tap_change_button(View.Changepassword))
        change_password_button.pack()

    def __fire_alert(self):
        self.__alert_fire.configure(text = self.Constants.alert_text, fg = self.Constants.fg)

    def __cease_fire_alert(self):
        self.__alert_fire.configure(text = self.Constants.no_fire)

    def __did_tap_change_button(self, view):
        if self.__change_view_handler is None:
            return
        self.__change_view_handler(view)

    def function(self, function):
        do_function = self.__functions[function]
        do_function()