from tkinter import Frame, Label, Button, N, S, E, W
from CustomType.View import View

class Room4View(Frame):
    def __init__(self, parent, change_view_handler = None):
        super().__init__(parent)
        self.__change_view_handler = change_view_handler

        room4_label = Label(self, text = "Habitacion 4")
        room4_label.pack(pady = 2, padx = 2)
        self.__configure_room4_UI()

        button1 = Button(self, text = "Back Home", command = lambda: self.__did_tap_change_button(View.Home))
        button1.pack(pady = 2, padx = 2)

    def __configure_room4_UI(self):
        pass

    def __did_tap_change_button(self, view):
        if self.__change_view_handler is None:
            return
        self.__change_view_handler(view)