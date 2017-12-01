class TemperatureModel():

    class Constants:
        top_temperature = 50
        max_temperature = 25

    def __init__(self, room, room_handler = None):
        self.__room = room
        self.__room_handler = room_handler
        self.__last_instruction = False

    def update_temperatures(self, temperature):
        if temperature > self.Constants.top_temperature: return
        self.__celsius = temperature
        self.__farenheit = temperature * (9 / 5) + 32
        self.__room.update_status(self.__celsius, self.__farenheit)
        self.__fan_on = self.__room.fan_status
        if self.__fan_on == False:
            if temperature >= self.Constants.max_temperature:
                self.__turn_on = True
                instruction = "{}_on".format(self.__room)
            else:
                self.__turn_on = False
                instruction = "{}_off".format(self.__room)
            if self.__last_instruction == self.__turn_on: return
            self.__last_instruction = self.__turn_on
            self.__room_handler(instruction)