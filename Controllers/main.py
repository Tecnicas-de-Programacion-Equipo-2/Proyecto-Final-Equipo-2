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
        self.temperature_room1 = TemperatureController(self.__master.container, self.__did_change_view,
                                                       '1', temperature_handler = self.__update_fan)
        self.temperature_room2 = TemperatureController(self.__master.container, self.__did_change_view,
                                                       '2', temperature_handler = self.__update_fan)

        self.__arduino = ArduinoModel(self.__master, self.temperature_room1, self.temperature_room2)
        self.home = HomeView(self.__master.container, change_view_handler=self.__did_change_view)
        self.temperature = TemperatureView(self.__master.container, change_view_handler=self.__did_change_view,
                                           tap_handler=self.__toggle_did_change)

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

    def __update_clock(self):
        try:
            data = self.__arduino.readline().decode()
        except UnicodeDecodeError:
            data = '0'
        self.__handle_data(data)
        self.__master.after(1, self.__update_clock)

    def __handle_data(self, data):
        clean_values = data.strip(' \n\r').split(', ')
        try:
            temperature = int(clean_values[0])
        except Exception:
            return
        self.temperature.update_temperatures(temperature)
        if temperature >= 28:
            print("******************" * 5)
            print("Encender Ventiladores")
            print("Temperature: ", temperature)

    def __toggle_did_change(self, state, device):
        value = str(1 if state else 0).encode('ascii')
        print (device, value)
        #self.__arduino.write(value)

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