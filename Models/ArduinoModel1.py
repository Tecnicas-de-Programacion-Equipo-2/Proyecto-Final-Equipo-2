from CustomType.Functions import Functions
from serial.tools import list_ports
from serial import Serial

class ArduinoModel1():

    class Constants:
        port = 'COM5'
        encode = 'ascii'

        baud = 115200

    def __init__(self, master, room1_model, room2_model, home):
        for port in list_ports.comports():
            print(port.device, port.name, port.description)

        self.__master = master
        self.__arduino = Serial(self.Constants.port, self.Constants.baud)

        self.__room1_model = room1_model
        self.__room2_model = room2_model

        self.__home = home

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
        self.__master.after(5, self.__update_clock)

    def __handle_data(self, data):
        clean_values = data.strip(' \n\r').split(', ')
        try:
            temperature_room1 = int(clean_values[0])
            temperature_room2 = int(clean_values[1])
            humidity_room1 = int(clean_values[2])
            humidity_room2 = int(clean_values[3])
            distance_alarm = int(clean_values[4])
        except Exception:
            return
        self.__room1_model.update_temperatures(temperature_room1)
        self.__room2_model.update_temperatures(temperature_room2)
        self.__home.update_humidity(humidity_room1)
        self.__home.update_humidity(humidity_room2)
        self.__home.update_distance(distance_alarm)

    def __close(self):
        self.__arduino.close()

    def turn_fan(self, instruction):
        turn_on = str(instruction).encode(self.Constants.encode)
        self.__arduino.write(turn_on)

    def function(self, function):
        do_function = self.__functions[function]
        do_function()