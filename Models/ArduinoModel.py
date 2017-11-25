from serial import Serial
from serial.tools import list_ports

class ArduinoModel():
    def __init__(self, master, temperature_room1, temperature_room2):
        for port in list_ports.comports():
            print(port.device, port.name, port.description)

        self.__master = master
        self.__arduino = Serial('COM4', 115200)

        self.__temperature_room1 = temperature_room1
        self.__temperature_room2 = temperature_room2

    def update_clock(self):
        try:
            data = self.__arduino.readline().decode()
        except UnicodeDecodeError:
            data = '0'
        self.__handle_data(data)
        self.__master.after(1, self.update_clock)

    def __handle_data(self, data):
        clean_values = data.strip(' \n\r').split(', ')
        try:
            temperature_room1 = int(clean_values[0])
            temperature_room2 = int(clean_values[1])
        except Exception:
            return
        self.__temperature_room1.update_temperatures(temperature_room1)
        self.__temperature_room2.update_temperatures(temperature_room2)

    def close(self):
        self.__arduino.close()