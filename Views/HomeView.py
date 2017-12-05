from tkinter import Frame, Label, Button
from CustomType.Functions import Functions
from CustomType.View import View

class HomeView(Frame):

    class Constants:
        home = 'Home'
        room_1 = 'Habitacion 1'
        room_2 = 'Habitacion 2'
        room_3 = 'Habitacion 3'
        room_4 = 'Habitacion 4'
        change = 'Cambiar contraseña o agregar tag'
        fg = '#d80808'
        alert_fire = 'INCENDIO DETECTADO'
        alert_intruder = 'INTRUSO DETECTADO'
        no_alert = ''
        fire_SMS = 'Tu casa ha detectado un incendio'
        intruder_SMS = 'Tu casa ha detectado un intruso'
        close = 'Cerrar puerta'

        pad_backend = 10

    def __init__(self, parent, change_view_handler = None, send_handler = None, close_door = None):
        super().__init__(parent)

        self.__change_view_handler = change_view_handler
        self.__send_handler = send_handler
        self.__close_door = close_door

        self.__last_fire_alert = False
        self.__last_intruder_alert = False

        self.__phone = '+525548557963'

        self.__configure_home_UI()

        self.__functions = {
            Functions.FireAlert: self.__fire_alert,
            Functions.CeaseFireAlert: self.__cease_fire_alert,
            Functions.IntruderAlert: self.__intruder_alert,
            Functions.CeaseIntruderAlert: self.__cease_intruder_alert
        }

    def __configure_home_UI(self):
        label = Label(self, text = self.Constants.home)
        label.pack(pady = self.Constants.pad_backend, padx = self.Constants.pad_backend)

        self.__alert_fire = Label(self, text = self.Constants.no_alert)
        self.__alert_fire.pack(padx = self.Constants.pad_backend, pady = self.Constants.pad_backend)

        self.__alert_intruder = Label(self, text = self.Constants.no_alert)
        self.__alert_intruder.pack(padx = self.Constants.pad_backend, pady = self.Constants.pad_backend)

        button = Button(self, text = self.Constants.room_1,
                        command = lambda: self.__did_tap_change_button(View.Room1))
        button.pack()
        button = Button(self, text = self.Constants.room_2,
                        command = lambda: self.__did_tap_change_button(View.Room2))
        button.pack()
        button = Button(self, text = self.Constants.room_3,
                        command = lambda: self.__did_tap_change_button(View.Room3))
        button.pack()
        button = Button(self, text = self.Constants.room_4,
                        command = lambda: self.__did_tap_change_button(View.Room4))
        button.pack()

        change_password_button = Button(self, text = self.Constants.change,
                    command = lambda: self.__did_tap_change_button(View.Changepassword))
        change_password_button.pack()

        close_door_button = Button(self, text = self.Constants.close, command = self.__close)
        close_door_button.pack()

    def __fire_alert(self):
        self.__fire = True
        if self.__last_fire_alert == self.__fire: return
        self.__send(self.Constants.fire_SMS)
        self.__last_fire_alert = self.__fire
        self.__alert_fire.configure(text = self.Constants.alert_fire, fg = self.Constants.fg)

    def __cease_fire_alert(self):
        self.__last_fire_alert = False
        self.__alert_fire.configure(text = self.Constants.no_alert)

    def __intruder_alert(self):
        self.__intruder = True
        if self.__last_intruder_alert == self.__intruder: return
        self.__send(self.Constants.intruder_SMS)
        self.__last_intruder_alert = self.__intruder
        self.__alert_intruder.configure(text = self.Constants.alert_intruder, fg = self.Constants.fg)

    def __cease_intruder_alert(self):
        self.__last_intruder_alert = False
        self.__alert_intruder.configure(text = self.Constants.no_alert)

    def __did_tap_change_button(self, view):
        if self.__change_view_handler is None:
            return
        self.__change_view_handler(view)

    def function(self, function):
        do_function = self.__functions[function]
        do_function()

    def __send(self, message):
        if self.__send_handler is None: return
        self.__send_handler(self.__phone, message)

    def __close(self):
        self.__close_door('DoorC')