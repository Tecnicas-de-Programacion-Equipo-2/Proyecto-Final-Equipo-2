from tkinter import Button, Label, PhotoImage

class ToggleButton(Label):
    class Constants:
        event = '<Button-1>'

    def __init__(self, master, room, image_on, image_off, tap_toggle_handler = None):
        super().__init__(master)
        self.__room = room
        self.__device_on = False
        self.__tap_toggle_handler = tap_toggle_handler

        #self.__on_image = PhotoImage(file = image_on)
        #self.__off_image = PhotoImage(file = image_off)
        #self.__set_image(self.__off_image)

        self.button = Button(self.master, bg='gray', text = 'Encender {}'.format(self.__room))
        self.button.pack()
        self.button.bind(self.Constants.event, self.__toggle)

    def __set_image(self,image):
        self.configure(image = image)
        self.image = image

    def __toggle(self, event):
        if self.__device_on is False:
            self.button.configure(bg='yellow', text='Apagar {}'.format(self.__room))
        else:
            self.button.configure(bg='gray', text='Encender {}'.format(self.__room))

        self.__device_on = not self.__device_on
        #image = self.__on_image if self.__state else self.__off_image
        #self.__set_image(image)

        if self.__tap_toggle_handler is None:
            return
        self.__tap_toggle_handler(self.__device_on, self.__room)

