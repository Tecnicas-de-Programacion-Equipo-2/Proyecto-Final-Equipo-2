from tkinter import Frame, Label, Button, N, S, E, W
from Views.ToggleButtons import ToggleButton
from CustomType.View import View

class Room2View(Frame):

    class Constants:
        heigth = 100
        width = 550
        center = N + S + E + W
        fan_on = 'Assets/fanon.ppm'
        fan_off = 'Assets/fanoff.ppm'
        room_fan_on = 'Turn on fan'
        room_fan_off = 'Turn off fan'
        color_on = 'limegreen'
        color_off = 'darkgray'

    def __init__(self, parent, tap_handler, change_view_handler = None):
        super().__init__(parent)
        self.__tap_fan_handler = tap_handler
        self.__change_view_handler = change_view_handler

        room2_label = Label(self, text = "Habitacion 2")
        room2_label.pack(pady = 2, padx = 2)
        self.__configure_room2_UI()

        button1 = Button(self, text = "Back Home", command = lambda: self.__did_tap_change_button(View.Home))
        button1.pack(pady = 2, padx = 2)

        self.__fan_on_button = ToggleButton(self, '2', self.Constants.fan_on, self.Constants.room_fan_on,
                                            self.Constants.color_on, tap_toggle_handler = self.__tap_fan_handler)
        self.__fan_off_button = ToggleButton(self, '2', self.Constants.fan_off, self.Constants.room_fan_off,
                                             self.Constants.color_off, tap_toggle_handler = self.__tap_fan_handler)

    def __configure_room2_UI(self):
        self.__celsius_room2 = Label(self)
        self.__celsius_room2.pack(pady = 1, padx = 1)

        self.__farenheit_room2 = Label(self)
        self.__farenheit_room2.pack(pady = 5, padx = 5)

    def update_status(self, celsius, farenheit):
        self.__celsius_room2.configure(text = "Temperature Celsius: " + "{0:.1f}".format(celsius) + " °C")
        self.__farenheit_room2.configure(text = "Temperature Farenheit: " + "{0:.1f}".format(farenheit) + " °F")

    def __did_tap_change_button(self, view):
        if self.__change_view_handler is None:
            return
        self.__change_view_handler(view)

    @property
    def fan_on(self):
        return self.__fan_on_button.fan_on

    @property
    def fan_off(self):
        return not (self.__fan_off_button.fan_on)