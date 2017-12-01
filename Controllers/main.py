from CustomType.Functions import Functions
from CustomType.View import View
from Models.ArduinoModel1 import ArduinoModel1
from Models.LEDModel import LEDModel
from Models.TemperatureModel import TemperatureModel
from Views.ChangepasswordView import Changepassword
from Views.ContainerView import ContainerView
from Views.HomeView import HomeView
from Views.PasswordView import PasswordView
from Views.Room1View import Room1View
from Views.Room2View import Room2View
from Views.Room3View import Room3View
from Views.Room4View import Room4View


class MainApp():

    class Constants:
        close_event = 'WM_DELETE_WINDOW'
        room_1 = '1'
        room_2 = '2'

    def __init__(self):
        self.__master = ContainerView()
        self.__master.protocol(self.Constants.close_event, self.__on_closing)

        self.password = PasswordView(self.__master.container, change_view_handler = self.__did_change_view)
        self.changepassword = Changepassword(self.__master.container, change_view_handler = self.__did_change_view)

        self.home = HomeView(self.__master.container, change_view_handler = self.__did_change_view)

        self.room1 = Room1View(self.__master.container, tap_handler = self.__update_fan,
                               change_view_handler = self.__did_change_view, slider_handler = self.__change_value_slider)
        self.room2 = Room2View(self.__master.container, tap_handler = self.__update_fan,
                               change_view_handler = self.__did_change_view, slider_handler = self.__change_value_slider)
        self.room3 = Room3View(self.__master.container, change_view_handler = self.__did_change_view,
                               slider_handler = self.__change_value_slider)
        self.room4 = Room4View(self.__master.container, change_view_handler = self.__did_change_view,
                               slider_handler = self.__change_value_slider)

        self.__room1_model = TemperatureModel(self.room1, room_handler = self.__update_fan)
        self.__room2_model = TemperatureModel(self.room2, room_handler = self.__update_fan)

        self.__arduino_1 = ArduinoModel1(self.__master, self.__room1_model, self.__room2_model, self.home)
        #self.__arduino_2 = ArduinoModel2(self.__master, self.changepassword, house_acces = self.password.try_card)

        self.__led = LEDModel()

        self.__frames = {
            View.Password: self.password,
            View.Changepassword: self.changepassword,
            View.Home: self.home,
            View.Room1: self.room1,
            View.Room2: self.room2,
            View.Room3: self.room3,
            View.Room4: self.room4
        }

        self.__master.set_views(self.__frames.values())
        self.__did_change_view(View.Password)

    def run(self):
        self.__arduino_1.function(Functions.UpdateClockArduino1)
        #self.__arduino_2.function(Functions.UpdateClockArduino2)
        self.__master.mainloop()

    def __on_closing(self):
        self.__arduino_1.function(Functions.CloseArduino1)
        #self.__arduino_2.function(Functions.CloseArduino2)
        self.__master.destroy()

    def __did_change_view(self, view):
        frame = self.__frames[view]
        frame.tkraise()

    def __change_value_slider(self, room, value):
        Data = [room, value]
        self.__led.read_brightness(Data)
        self.__led_instruction = self.__led.get_instruction
        print(self.__led_instruction)
        #self.__arduino_2.send_led_values(self.__led_instruction)

    def __update_fan(self, instruction):
        print(instruction)
        self.__arduino_1.turn_fan(instruction)

if __name__ == "__main__":
    app = MainApp()
    app.run()