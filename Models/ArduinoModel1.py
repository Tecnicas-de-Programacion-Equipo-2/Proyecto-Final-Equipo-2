from CustomType.Functions import Functions
from serial.tools import list_ports
from serial import Serial

class ArduinoModel1():

    class Constants:
        port = 'COM4'

        baud = 115200

    def __init__(self, master, temperature_room1, temperature_room2):
        for port in list_ports.comports():
            print(port.device, port.name, port.description)

        self.__master = master
        self.__arduino = Serial(self.Constants.port, self.Constants.baud)

        self.__temperature_room1 = temperature_room1
        self.__temperature_room2 = temperature_room2

        self.__functions = {
            Functions.UpdateClock: self.__update_clock,
            Functions.Close: self.__close,
            Functions.TurnFan: self.__turn_fan,
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

    def __turn_fan(self, instruction):
        turn_on = str(instruction).encode(self.Constants.encode)
        print(str(turn_on))
        self.__arduino.write(turn_on)

    def function(self, function):
        do_function = self.__functions[function]
        do_function()