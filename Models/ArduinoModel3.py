from CustomType.Functions import Functions
from serial.tools import list_ports
from serial import Serial

class ArduinoModel3():

    class Constants:
        port = "COM3"
        baud = 9600

    def __init__(self, master, distance):
        for port in list_ports.comports():
            print(port.device, port.name, port.description)

        self.__master = master
        self.__arduino = Serial(self.Constants.port, self.Constants.baud)

        self.__distance = distance

        self.__functions = {
            Functions.UpdateClock: self.__update_clock,
            Functions.Close: self.__close,
            Functions.TurnFan: self.__turn_fan
        }

    def __update_clock(self):
        try:
            data = self.__arduino.readline().decode()
        except UnicodeDecodeError:
            data = '0'
        self.__handle_data(data)
        self.__master.after(1, self.__update_clock)

    def __handle_data(self, data):
        clean_values = data.strip(' \n\r').split(', ')
        try:
            distance = float(clean_values[0])
        except Exception:
            return
        self.__distance.update_distance(distance)

    def __close(self):
        self.__arduino.close()

    def function(self, function):
        do_function = self.__functions[function]
        do_function()