from Controllers.TemperatureController import TemperatureController
from Models.ArduinoModel import ArduinoModel
from Views.ContainerView import ContainerView
from Views.HomeView import HomeView
from CustomType.View import View
from CustomType.Functions import Functions

class MainApp():

    class Constants:
        close_event = "WM_DELETE_WINDOW"

    def __init__(self):
        self.__master = ContainerView()
        self.__master.protocol(self.Constants.close_event, self.__on_closing)

        self.home = HomeView(self.__master.container, change_view_handler = self.__did_change_view)
        self.temperature_room1 = TemperatureController(self.__master.container, self.__did_change_view, '1')
        self.temperature_room2 = TemperatureController(self.__master.container, self.__did_change_view, '2')

        self.__arduino = ArduinoModel(self.__master, self.temperature_room1, self.temperature_room2)

        self.__frames = {
            View.Home: self.home,
            View.TemperatureRoom1: self.temperature_room1.temperature,
            View.TemperatureRoom2: self.temperature_room2.temperature
        }

        self.__master.set_views(self.__frames.values())
        self.__did_change_view(View.Home)

    def run(self):
        self.__arduino.function(Functions.UpdateClock)
        self.__master.mainloop()

    def __on_closing(self):
        self.__arduino.function(Functions.Close)
        self.__master.destroy()

    def __did_change_view(self, view):
        frame = self.__frames[view]
        frame.tkraise()

if __name__ == "__main__":
    app = MainApp()
    app.run()