
from tkinter import Frame, Label, Button, N, S, E, W
from CustomType.View import View
from Views.ToggleButtons import ToggleButton

class TemperatureView(Frame):
    class Constants:
        heigth = 100
        width = 550
        center = N + S + E + W
        fan_on = 'Assets/fanon.ppm'
        fan_off = 'Assets/fanoff.ppm'
        room_fan_1 = 'ventilador cuarto 1'
        room_fan_2 = 'ventilador cuarto 2'

    def __init__(self, parent, change_view_handler = None, tap_handler = None):
        super().__init__(parent)
        self.__change_view_handler = change_view_handler
        self.__initial_celsius = 0
        self.__initial_farenheit = 0
        self.__configure_UI()
        button1 = Button(self, text = "Back to Home", command = lambda: self.__did_tap_change_button(View.Home))
        button1.pack()

        self.__fan_1_button = ToggleButton(self, self.Constants.room_fan_1, self.Constants.fan_on,
                                           self.Constants.fan_off, tap_toggle_handler = tap_handler)
        self.__fan_2_button = ToggleButton(self, self.Constants.room_fan_2, self.Constants.fan_on,
                                           self.Constants.fan_off, tap_toggle_handler = tap_handler)

    def __configure_UI(self):
        self.__celsius_label = Label(self)
        self.__celsius_label.configure(text = "Temperature Celsius: °C")
        self.__celsius_label.pack(pady = 10, padx = 10)

        self.__farenheit_label = Label(self)
        self.__farenheit_label.configure(text = "Temperature Farenheit: °F")
        self.__farenheit_label.pack(pady = 10, padx = 10)

    def __did_tap_change_button(self, view):
        if self.__change_view_handler is None:
            return
        self.__change_view_handler(view)

    def update_temperatures(self, value):
        print("Value: ", value)
        self.__celsius_label.configure(text = "Temperature Celsius: " + "{0:.1f}".format(value) + " °C")
        self.__farenheit_label.configure(text = "Temperature Farenheit: " + "{0:.1f}".format(value * (9 / 5) + 32) + " °F")
