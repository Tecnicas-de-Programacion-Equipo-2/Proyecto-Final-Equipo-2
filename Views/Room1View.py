from tkinter import Frame, Label, Button, N, S, E, W
from Views.ToggleButtons import ToggleButton
from CustomType.View import View

class Room1View(Frame):
    class Constants:
        heigth = 100
        width = 550
        center = N + S + E + W
        fan_on = 'Assets/on.ppm'
        fan_off = 'Assets/off.ppm'
        room_fan_on = 'Fan on'
        room_fan_off = 'Fan off'

    def __init__(self, parent, tap_handler, change_view_handler = None):
        super().__init__(parent)
        self.__fan_on = False
        self.__tap_fan_handler = tap_handler
        self.__change_view_handler = change_view_handler
        room1_label = Label(self, text = "Habitacion 1")
        room1_label.pack(pady = 2, padx = 2)
        self.__configure_room1_UI()

        button2 = Button(self, text = "Back Home", command = lambda: self.__did_tap_change_button(View.Home))
        button2.pack(pady = 2, padx = 2)

        self.__fan_button = ToggleButton(self, '1', self.Constants.fan_on, self.Constants.room_fan_on,
                                            self.Constants.fan_off, self.Constants.room_fan_off,
                                         tap_toggle_handler = self.__tap_fan_handler)

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

    @property
    def fan_status(self):
        self.__fan_on = self.__fan_button.fan_on
        return (self.__fan_on)