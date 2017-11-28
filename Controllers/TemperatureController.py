from Views.Room1View import Room1View
from Views.Room2View import Room2View

class TemperatureController():

    def __init__(self, container, did_change_view, room_number, room_handler = None):
        self.__did_change_view = did_change_view
        self.__room_handler = room_handler
        self.__room = room_number

        if room_number == '1':
            self.room = Room1View(container, self.__room_handler,
                                         change_view_handler = self.__did_change_view)
        if room_number == '2':
            self.room = Room2View(container, self.__room_handler,
                                         change_view_handler = self.__did_change_view)

    def update_temperatures(self, temperature):
        if temperature > 50: return
        self.__celsius = temperature
        self.__farenheit = temperature * (9 / 5) + 32
        self.room.update_status(self.__celsius, self.__farenheit)
        self.__fan_on = self.room.fan_status
        if self.__fan_on == False:
            if temperature >= 28:
                self.__turn_on = True
                instruction = "{}_on".format(self.__room)
            else:
                self.__turn_on = False
                instruction = "{}_off".format(self.__room)
            self.__room_handler(instruction)