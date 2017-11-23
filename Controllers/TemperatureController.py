from Views.TemperatureView import TemperatureView

class TemperatureController():
    def __init__(self, container, did_change_view):
        self.__did_change_view = did_change_view
        self.temperature = TemperatureView(container, change_view_handler = self.__did_change_view)
        self.__is_room1 = True

    def update_temperatures(self, value):
        self.__celsius = value
        self.__farenheit = value * (9 / 5) + 32
        if self.__is_room1:
            self.temperature.update_room1_status(self.__celsius, self.__farenheit)
            self.__is_room1 = False
        else:
            self.temperature.update_room2_status(self.__celsius, self.__farenheit)
            self.__is_room1 = True