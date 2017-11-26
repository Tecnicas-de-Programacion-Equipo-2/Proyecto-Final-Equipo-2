from tkinter import Frame, Label, Button, N, S, E, W
from CustomType.View import View

class Room1View(Frame):

    class Constants:
        heigth = 100
        width = 550
        center = N + S + E + W

    def __init__(self, parent, change_view_handler = None):
        super().__init__(parent)
        self.__change_view_handler = change_view_handler

        room1_label = Label(self, text = "Habitacion 1")
        room1_label.pack(pady = 2, padx = 2)
        self.__configure_room1_UI()

        button1 = Button(self, text= "Temperature Room 2",
                         command = lambda: self.__did_tap_change_button(View.TemperatureRoom2))
        button1.pack(pady = 2, padx = 2)
        button2 = Button(self, text = "Back to Home", command = lambda: self.__did_tap_change_button(View.Home))
        button2.pack(pady = 2, padx = 2)

    def __configure_room1_UI(self):
        self.__celsius_room1 = Label(self)
        self.__celsius_room1.pack(pady = 1, padx = 1)

        self.__farenheit_room1 = Label(self)
        self.__farenheit_room1.pack(pady = 1, padx = 1)

    def update_status(self, celsius, farenheit):
        self.__celsius_room1.configure(text = "Temperature Celsius: " + "{0:.1f}".format(celsius) + " °C")
        self.__farenheit_room1.configure(text = "Temperature Farenheit: " + "{0:.1f}".format(farenheit) + " °F")

    def __did_tap_change_button(self, view):
        if self.__change_view_handler is None:
            return
        self.__change_view_handler(view)