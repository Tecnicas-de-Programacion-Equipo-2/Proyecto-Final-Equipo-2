class LEDModel():

    class Constants:
        encode = 'ascii'

    def __init__(self):
        self.__value_room_1 = str('0').encode(self.Constants.encode)
        self.__value_room_2 = str('0').encode(self.Constants.encode)
        self.__value_room_3 = str('0').encode(self.Constants.encode)
        self.__value_room_4 = str('0').encode(self.Constants.encode)

    def read_brightness(self, data):
        self.__data = data

        if self.__data[0] == '1':
            self.__value_room_1 = self.__data[1]
            self.__value_room_1 = str(self.__value_room_1).encode(self.Constants.encode)
        if self.__data[0] == '2':
            self.__value_room_2 = self.__data[1]
            self.__value_room_2 = str(self.__value_room_2).encode(self.Constants.encode)
        if self.__data[0] == '3':
            self.__value_room_3 = self.__data[1]
            self.__value_room_3 = str(self.__value_room_3).encode(self.Constants.encode)
        if self.__data[0] == '4':
            self.__value_room_4 = self.__data[1]
            self.__value_room_4 = str(self.__value_room_4).encode(self.Constants.encode)

        self.__instruction = '{} {} {} {}'.format(self.__value_room_1, self.__value_room_2,
                                           self.__value_room_3, self.__value_room_4)

    @property
    def get_instruction(self):
        return self.__instruction