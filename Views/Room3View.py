from tkinter import Frame, Label, Button
from CustomType.View import View

class Room3View(Frame):

    class Constants:
        title = 'Habitacion 3'
        room = '3'
        update = 'Encender Luz'
        back = 'Back Home'
        color_on = 'limegreen'
        color_off = 'darkgray'
        led_off = 'LED Apagado'
        led_on = 'LED Encendido'
        off = '3_off'
        on = '3_on'

        fromled = 0
        to = 255
        pad_middle = 2
        pad_backend = 4

        event = '<Button-1>'

    def __init__(self, parent, change_view_handler = None, slider_handler = None):
        super().__init__(parent)
        self.__change_view_handler = change_view_handler
        self.__slider_handler = slider_handler
        self.__value = False

        self.__configure_room3_UI()

    def __configure_room3_UI(self):
        self.__room3_label = Label(self, text = self.Constants.title)
        self.__room3_label.pack(pady = self.Constants.pad_backend, padx = self.Constants.pad_backend)

        self.__button_led = Button(self, text = self.Constants.led_off, bg = self.Constants.color_off)
        self.__button_led.bind(self.Constants.event, self.__change_value)
        self.__button_led.pack(pady = self.Constants.pad_middle, padx = self.Constants.pad_middle)

        self.__button_back = Button(self, text = self.Constants.back,
                                    command = lambda: self.__did_tap_change_button(View.Home))
        self.__button_back.pack(pady = self.Constants.pad_backend, padx = self.Constants.pad_backend)

    def __did_tap_change_button(self, view):
        if self.__change_view_handler is None:
            return
        self.__change_view_handler(view)

    def __change_value(self, event):
        if self.__slider_handler is None: return
        self.__value = not self.__value
        if self.__value:
            self.__led_change = self.Constants.on
            self.__button_led.configure(bg = self.Constants.color_on, text = self.Constants.led_on)
        else:
            self.__led_change = self.Constants.off
            self.__button_led.configure(bg = self.Constants.color_off, text = self.Constants.led_off)
        self.__slider_handler(self.Constants.room, self.__led_change)