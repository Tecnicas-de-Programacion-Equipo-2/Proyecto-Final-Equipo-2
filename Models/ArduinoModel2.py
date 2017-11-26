from CustomType.Functions import Functions
from serial.tools import list_ports
from serial import Serial

class ArduinoModel2():

    class Constants:
        port = "COM6"
        baud = 115200

    def __init__(self, master):
        for port in list_ports.comports():
            print(port.device, port.name, port.description)

        self.__master = master
        self.__arduino = Serial(self.Constants.port, self.Constants.baud)

        self.__functions = {
            Functions.UpdateClock: self.__update_clock,
            Functions.Close: self.__close
        }

    def __update_clock(self):
        try:
            data = self.__arduino.readline().decode()
        except UnicodeDecodeError:
            data = '0'
        self.__handle_data(data)
        self.__master.after(1, self.__update_clock)

    def __handle_data(self, data):
        try:
            password_from_tag = int(data)
            print(password_from_tag)
        except Exception:
            return

    def __close(self):
        self.__arduino.close()

    def function(self, function):
        do_function = self.__functions[function]
        do_function()