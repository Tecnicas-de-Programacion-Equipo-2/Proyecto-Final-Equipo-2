from tkinter import Frame, Label, Scale, Button, HORIZONTAL
from CustomType.View import View

class Room3View(Frame):

    class Constants:
        title = 'Habitacion 3'
        room = '3'
        update = 'Actualizar Brillo'
        back = 'Back Home'

        fromled = 0
        to = 255
        pad_middle = 2
        pad_backend = 4

        event = '<Button-1>'

    def __init__(self, parent, change_view_handler = None, slider_handler = None):
        super().__init__(parent)
        self.__change_view_handler = change_view_handler
        self.__slider_handler = slider_handler
        self.__configure_room3_UI()

    def __configure_room3_UI(self):
        self.__room3_label = Label(self, text = self.Constants.title)
        self.__room3_label.pack(pady = self.Constants.pad_backend, padx = self.Constants.pad_backend)

        self.__brightness_led = Scale(self, from_ = self.Constants.fromled,
                                      to = self.Constants.to, orient = HORIZONTAL, length = self.Constants.to)
        self.__brightness_led.set(self.Constants.fromled)
        self.__brightness_led.pack(pady = self.Constants.pad_middle, padx = self.Constants.pad_middle)

        self.__button_change = Button(self, text = self.Constants.update)
        self.__button_change.bind(self.Constants.event, self.__change_value)
        self.__button_change.pack(pady = self.Constants.pad_middle, padx = self.Constants.pad_middle)

        self.__button_back = Button(self, text = self.Constants.back,
                                command = lambda: self.__did_tap_change_button(View.Home))
        self.__button_back.pack(pady = self.Constants.pad_backend, padx = self.Constants.pad_backend)

    def __did_tap_change_button(self, view):
        if self.__change_view_handler is None:
            return
        self.__change_view_handler(view)

    def __change_value(self, event):
        if self.__slider_handler is None: return
        self.__state = self.__brightness_led.get()
        self.__slider_handler(self.Constants.room, self.__state)