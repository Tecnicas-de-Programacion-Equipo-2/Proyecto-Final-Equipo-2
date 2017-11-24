from Models.FanModel import FanModel
from Views.Room1View import Room1View
from Views.Room2View import Room2View

class TemperatureController():
    def __init__(self, container, did_change_view, room):
        self.__fan = FanModel()
        self.__did_change_view = did_change_view
        self.__room = room

        if room == '1':
            self.temperature = Room1View(container, change_view_handler = self.__did_change_view)
        if room == '2':
            self.temperature = Room2View(container, change_view_handler = self.__did_change_view)

    def update_temperatures(self, value):
        self.__celsius = value
        self.__farenheit = value * (9 / 5) + 32
        self.temperature.update_status(self.__celsius, self.__farenheit)
        if value >= 28:
            self.turn_on_fan()

    def turn_on_fan(self):
        self.__fan.turn_on()