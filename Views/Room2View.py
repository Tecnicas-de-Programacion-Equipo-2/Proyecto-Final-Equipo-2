from tkinter import Frame, Label, Button, Scale, HORIZONTAL
from Views.ToggleButtons import ToggleButton
from CustomType.View import View

class Room2View(Frame):
    class Constants:
        fan_on = 'Assets/on.ppm'
        fan_off = 'Assets/off.ppm'
        room_fan_on = 'Fan on'
        room_fan_off = 'Fan off'
        title = 'Habitacion 2'
        room = '2'
        update = 'Actualizar Brillo'
        back = 'Back Home'
        celsius = 'Temperature Celsius: '
        celsius_symbol = ' °C'
        farenheit = 'Temperature Farenheit: '
        farenheit_symbol = ' °F'

        fromled = 0
        to = 255
        pad_middle = 2
        pad_backend = 4

        event = '<Button-1>'

    def __init__(self, parent, tap_handler, change_view_handler = None, slider_handler = None):
        super().__init__(parent)
        self.__fan_on = False
        self.__tap_fan_handler = tap_handler
        self.__slider_handler = slider_handler
        self.__change_view_handler = change_view_handler
        self.__bright_change = self.Constants.fromled

        self.__configure_room2_UI()

    def __configure_room2_UI(self):
        room2_label = Label(self, text = self.Constants.title)
        room2_label.pack(pady = self.Constants.pad_backend, padx = self.Constants.pad_backend)

        self.__celsius_room2 = Label(self)
        self.__celsius_room2.pack(pady = self.Constants.pad_middle, padx = self.Constants.pad_middle)

        self.__farenheit_room2 = Label(self)
        self.__farenheit_room2.pack(pady = self.Constants.pad_middle, padx = self.Constants.pad_middle)

        self.__brightness_led = Scale(self, from_ = self.Constants.fromled,
                                      to = self.Constants.to, orient = HORIZONTAL, length = self.Constants.to)
        self.__brightness_led.set(self.__bright_change)
        self.__brightness_led.pack(pady = self.Constants.pad_middle, padx = self.Constants.pad_middle)

        self.__button_change = Button(self, text = self.Constants.update)
        self.__button_change.bind(self.Constants.event, self.__change_value)
        self.__button_change.pack(pady = self.Constants.pad_middle, padx = self.Constants.pad_middle)

        self.__fan_button = ToggleButton(self, self.Constants.room, self.Constants.fan_on,
                                         self.Constants.room_fan_on, self.Constants.fan_off,
                                         self.Constants.room_fan_off, tap_toggle_handler = self.__tap_fan_handler)
        self.__fan_button.pack(pady = self.Constants.pad_middle, padx = self.Constants.pad_middle)

        button1 = Button(self, text = self.Constants.back, command = lambda: self.__did_tap_change_button(View.Home))
        button1.pack(pady = self.Constants.pad_backend, padx = self.Constants.pad_backend)

    def update_status(self, celsius, farenheit):
        self.__celsius_room2.configure(text = self.Constants.celsius + "{0:.1f}".format(celsius) +
                                              self.Constants.celsius_symbol)
        self.__farenheit_room2.configure(text = self.Constants.farenheit + "{0:.1f}".format(farenheit) +
                                                self.Constants.farenheit_symbol)

    def __did_tap_change_button(self, view):
        if self.__change_view_handler is None:
            return
        self.__change_view_handler(view)

    def __change_value(self, event):
        if self.__slider_handler is None: return
        self.__value = self.__brightness_led.get()
        self.__bright_change = self.__value
        self.__slider_handler(self.Constants.room, self.__value)

    @property
    def fan_status(self):
        self.__fan_on = self.__fan_button.fan_on
        return (self.__fan_on)