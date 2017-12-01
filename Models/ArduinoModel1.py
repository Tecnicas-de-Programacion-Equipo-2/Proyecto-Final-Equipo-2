from CustomType.Functions import Functions
from serial.tools import list_ports
from serial import Serial

class ArduinoModel1():

    class Constants:
        port = 'COM5'
        encode = 'ascii'

        baud = 115200

    def __init__(self, master, temperature_room1, temperature_room2):
        for port in list_ports.comports():
            print(port.device, port.name, port.description)

        self.__master = master
        self.__arduino = Serial(self.Constants.port, self.Constants.baud)

        self.__temperature_room1 = temperature_room1
        self.__temperature_room2 = temperature_room2

        self.__functions = {
            Functions.UpdateClockArduino1: self.__update_clock,
            Functions.CloseArduino1: self.__close,
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
            temperature_room1 = int(clean_values[0])
            temperature_room2 = int(clean_values[1])
        except Exception:
            return
        self.__temperature_room1.update_temperatures(temperature_room1)
        self.__temperature_room2.update_temperatures(temperature_room2)

    def __close(self):
        self.__arduino.close()

    def turn_fan(self, instruction):
        turn_on = str(instruction).encode(self.Constants.encode)
        self.__arduino.write(turn_on)

    def function(self, function):
        do_function = self.__functions[function]
        do_function()