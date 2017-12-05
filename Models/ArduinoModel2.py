from CustomType.Functions import Functions
from serial.tools import list_ports
from serial import Serial

class ArduinoModel2():
    class Constants:
        port = 'COM9'
        encode = 'ascii'

        baud = 115200

    def __init__(self, master, change_password, house_acces=None):
        for port in list_ports.comports():
            print(port.device, port.name, port.description)

        self.__master = master
        self.__house_acces = house_acces
        self.__changepasswordview = change_password
        self.__arduino = Serial(self.Constants.port, self.Constants.baud)
        self.change_door("DoorC")

        self.__functions = {
            Functions.UpdateClockArduino2: self.__update_clock,
            Functions.CloseArduino2: self.__close,
        }

    def __update_clock(self):
        try:
            data = self.__arduino.readline().decode()
        except UnicodeDecodeError:
            data = '0'
        self.__handle_data(data)
        self.__master.after(4, self.__update_clock)

    def __handle_data(self, data):
        try:
            password_from_tag = int(data)
            if password_from_tag != 0:
                self.__house_acces(password_from_tag)
                self.__changepasswordview.new_card(password_from_tag)
        except Exception:
            return

    def send_led_values(self, instruction):
        instruction = instruction + self.__door_position
        self.__arduino.write(instruction)

    def change_door(self, instruction):
        change_position = str(instruction).encode(self.Constants.encode)
        self.__door_position = change_position

    def __close(self):
        self.__arduino.close()

    def function(self, function):
        do_function = self.__functions[function]
        do_function()