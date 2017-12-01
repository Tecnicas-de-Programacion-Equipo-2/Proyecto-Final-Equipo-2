from CustomType.Functions import Functions

class DistanceModel():

    class Constants:
        minimum_distance = -5

    def __init__(self, home):
        self.__home = home

    def update_distance(self, distance):
        if distance < self.Constants.minimum_distance:
            self.__home.function(Functions.IntruderAlert)
        else:
            self.__home.function(Functions.CeaseIntruderAlert)