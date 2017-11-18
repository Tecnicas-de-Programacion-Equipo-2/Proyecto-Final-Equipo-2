from tkinter import Frame, Label, Button, N, S, E, W
from CustomType.View import View

class ViewTemperature(Frame):
    class Constants:
        heigth = 100
        width = 550
        center = N + S + E + W

    def __init__(self, parent, change_view_handler = None):
        super().__init__(parent)
        self.__change_view_handler = change_view_handler
        self.__initial_celsius = 0
        self.__initial_farenheit = 0

        self.__configure_UI()

        button1 = Button(self, text = "Back to Home", command = lambda: self.__did_tap_change_button(View.Start))
        button1.pack()

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