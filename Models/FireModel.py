from CustomType.Functions import Functions

class FireModel():

    class Constants:
        minimum_humidity = 5

    def __init__(self, home):
        self.__home = home

    def update_humidity(self, humidity):
        if humidity < self.Constants.minimum_humidity:
            self.__home.function(Functions.FireAlert)
        else:
            self.__home.function(Functions.CeaseFireAlert)