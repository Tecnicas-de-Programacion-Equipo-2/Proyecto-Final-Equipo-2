class LEDModel():

    class Constants:
        encode = 'ascii'

    def __init__(self):
        self.__value_room_1 = '0'
        self.__value_room_2 = '0'
        self.__value_room_3 = '0'
        self.__value_room_4 = '0'

    def read_brightness(self, data):
        self.__data = data

        if self.__data[0] == '1': self.__value_room_1 = self.__data[1]
        if self.__data[0] == '2': self.__value_room_2 = self.__data[1]
        if self.__data[0] == '3': self.__value_room_3 = self.__data[1]
        if self.__data[0] == '4': self.__value_room_4 = self.__data[1]

        self.__instruction = '{} {} {} {}'.format(self.__value_room_1, self.__value_room_2,
                                                  self.__value_room_3, self.__value_room_4)
        self.__instruction = str(self.__instruction).encode(self.Constants.encode)

    @property
    def get_instruction(self):
        return self.__instruction