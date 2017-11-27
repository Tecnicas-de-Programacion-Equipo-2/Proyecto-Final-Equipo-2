from tkinter import Frame, Label, Button, N, S, E, W
from CustomType.View import View

class Room3View(Frame):
    def __init__(self, parent, change_view_handler = None):
        super().__init__(parent)
        self.__change_view_handler = change_view_handler

        room3_label = Label(self, text = "Habitacion 3")
        room3_label.pack(pady = 2, padx = 2)
        self.__configure_room3_UI()

        button1 = Button(self, text = "Back Home", command = lambda: self.__did_tap_change_button(View.Home))
        button1.pack(pady = 2, padx = 2)

    def __configure_room3_UI(self):
        pass

    def __did_tap_change_button(self, view):
        if self.__change_view_handler is None:
            return
        self.__change_view_handler(view)