from tkinter import Frame, Label, Button
from CustomType.View import View

class HomeView(Frame):
    def __init__(self, parent, change_view_handler = None):
        super().__init__(parent)

        self.__change_view_handler = change_view_handler

        label = Label(self, text = "Home")
        label.pack(pady = 10, padx = 10)

        button = Button(self, text = "Check Temperature", command = lambda: self.__did_tap_change_button(View.TemperatureRoom1))
        button.pack()

    def __did_tap_change_button(self, view):
        if self.__change_view_handler is None:
            return
        self.__change_view_handler(view)