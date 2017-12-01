from tkinter import Button, Label, PhotoImage

class ToggleButton(Label):
    class Constants:
        color_on = 'limegreen'
        color_off = 'darkgray'

        event = '<Button-1>'

    def __init__(self, master, room, image_on, text_button_on, image_off, text_button_off, tap_toggle_handler = None):
        super().__init__(master)
        self.__room = room
        self.fan_on = False
        self.__tap_toggle_handler = tap_toggle_handler
        self.__text_on = text_button_on
        self.__text_off = text_button_off
        self.__on_image = PhotoImage(file = image_on)
        self.__off_image = PhotoImage(file = image_off)

        self.button = Button(self.master, bg = self.Constants.color_off, text = self.__text_on, image=self.__on_image)
        self.button.pack()
        self.button.bind(self.Constants.event, self.__toggle)

    def __set_image(self,image):
        self.button.configure(image = image)
        self.image = image

    def __toggle(self, event):
        if self.fan_on == False:
            self.fan_on = True
            self.button.configure(bg = self.Constants.color_on, text = self.__text_on)
            instruction = "{}_on".format(self.__room)
        else:
            self.fan_on = False
            self.button.configure(bg = self.Constants.color_off, text = self.__text_off)
            instruction = "{}_off".format(self.__room)
        image = self.__off_image if self.fan_on else self.__on_image
        self.__set_image(image)
        if self.__tap_toggle_handler is None:
            return
        self.__tap_toggle_handler(instruction)