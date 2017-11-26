from tkinter import Button, Label, PhotoImage

class ToggleButton(Label):
    class Constants:
        event = '<Button-1>'

    def __init__(self, master, room, image, text_button, color_button, tap_toggle_handler = None):
        super().__init__(master)
        self.__room = room
        self.__type_of_button = text_button
        self.__tap_toggle_handler = tap_toggle_handler

        #self.__on_image = PhotoImage(file = image)

        self.button = Button(self.master, bg=color_button, text = self.__type_of_button)
        self.button.pack()
        self.button.bind(self.Constants.event, self.__toggle)

    def __toggle(self, event):
        if self.__type_of_button == 'Turn on fan':
            instruction = "{}_on".format(self.__room)
        else:
            instruction = "{}_off".format(self.__room)
        self.__tap_toggle_handler(instruction)

