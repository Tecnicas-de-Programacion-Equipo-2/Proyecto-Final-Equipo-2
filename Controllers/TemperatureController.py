from Views.Room1View import Room1View
from Views.Room2View import Room2View

class TemperatureController():

    def __init__(self, container, did_change_view, room, temperature_handler = None):
        self.__did_change_view = did_change_view
        self.__temperature_handler = temperature_handler
        self.__room = room

        if room == '1':
            self.temperature = Room1View(container, change_view_handler = self.__did_change_view)
        if room == '2':
            self.temperature = Room2View(container, change_view_handler = self.__did_change_view)

    def update_temperatures(self, value):
        if value > 50: return
        self.__celsius = value
        self.__farenheit = value * (9 / 5) + 32
        self.temperature.update_status(self.__celsius, self.__farenheit)
        if value >= 28:
            self.__turn_on = True
            instruction = "{}_on".format(self.__room)
        else:
            self.__turn_on = False
            instruction = "{}_off".format(self.__room)
        self.__temperature_handler(instruction)