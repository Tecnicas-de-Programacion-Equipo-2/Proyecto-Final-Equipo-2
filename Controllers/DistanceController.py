
class DistanceController():
    class Constants:
        dates = 50

    def __init__(self, values):
        super().__init__()
        self.__average = 0
        self.__sum = 0
        self.__distances(values)

    def __distances(self, value):
        for index in range(1, 50):
            self.__sum = self.__sum + float(value)
        self.__average = self.__sum / self.Constants.dates
        self.__sum = 0
        round(self.__average)

    def update_distance(self, distance):
        if distance < 5:
            self.__turn_on_alarm = True
        else:
            self.__turn_on_alarm = False





