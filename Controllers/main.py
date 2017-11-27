from Controllers.TemperatureController import TemperatureController
from Models.ArduinoModel1 import ArduinoModel1
from Models.ArduinoModel2 import ArduinoModel2
from Views.ContainerView import ContainerView
from Views.HomeView import HomeView
from Views.Room3View import Room3View
from Views.Room4View import Room4View
from Views.PasswordView import PasswordView
from CustomType.View import View
from CustomType.Functions import Functions

class MainApp():

    class Constants:
        close_event = "WM_DELETE_WINDOW"

    def __init__(self):
        self.__master = ContainerView()
        self.__master.protocol(self.Constants.close_event, self.__on_closing)

        self.password = PasswordView(self.__master.container, change_view_handler = self.__did_change_view)
        self.home = HomeView(self.__master.container, change_view_handler = self.__did_change_view)
        self.room1 = TemperatureController(self.__master.container, self.__did_change_view,
                                                       '1', room_handler = self.__update_fan)
        self.room2 = TemperatureController(self.__master.container, self.__did_change_view,
                                                       '2', room_handler = self.__update_fan)
        self.room3 = Room3View(self.__master.container, change_view_handler = self.__did_change_view)
        self.room4 = Room4View(self.__master.container, change_view_handler = self.__did_change_view)

        self.__arduino_1 = ArduinoModel1(self.__master, self.room1, self.room2)
        #self.__arduino_2 = ArduinoModel2(self.__master, house_acces = self.password.try_card)

        self.__frames = {
            View.Password: self.password,
            View.Home: self.home,
            View.Room1: self.room1.room,
            View.Room2: self.room2.room,
            View.Room3: self.room3,
            View.Room4: self.room4
        }

        self.__master.set_views(self.__frames.values())
        self.__did_change_view(View.Password)

    def run(self):
        self.__arduino_1.function(Functions.UpdateClock)
        #self.__arduino_2.function(Functions.UpdateClock)
        self.__master.mainloop()

    def __on_closing(self):
        self.__arduino_1.function(Functions.Close)
        #self.__arduino_2.function(Functions.Close)
        self.__master.destroy()

    def __did_change_view(self, view):
        frame = self.__frames[view]
        frame.tkraise()

    def __update_fan(self, instruction):
        #turn_fan = self.__arduino.function(Functions.TurnFan)
        #turn_fan()
        print(instruction)

if __name__ == "__main__":
    app = MainApp()
    app.run()