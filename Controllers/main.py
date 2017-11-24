from Controllers.TemperatureController import TemperatureController
from Views.ContainerView import ContainerView
from Views.HomeView import HomeView
from CustomType.View import View
from serial import Serial
from serial.tools import list_ports

class MainApp():

    def __init__(self):
        for port in list_ports.comports():
            print(port.device, port.name, port.description)

        self.__master = ContainerView()
        self.__arduino = Serial('COM4', 115200)
        self.__master.protocol("WM_DELETE_WINDOW", self.__on_closing)

        self.home = HomeView(self.__master.container, change_view_handler = self.__did_change_view)
        self.temperature_room1 = TemperatureController(self.__master.container, self.__did_change_view, '1')
        self.temperature_room2 = TemperatureController(self.__master.container, self.__did_change_view, '2')

        self.__frames = {
            View.Home: self.home,
            View.TemperatureRoom1: self.temperature_room1.temperature,
            View.TemperatureRoom2: self.temperature_room2.temperature
        }

        self.__master.set_views(self.__frames.values())
        self.__did_change_view(View.Home)

    def run(self):
        self.__update_clock()
        self.__master.mainloop()

    def __on_closing(self):
        self.__arduino.close()
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
            temperature_room1 = int(clean_values[0])
            temperature_room2 = int(clean_values[1])
        except Exception:
            return
        self.temperature_room1.update_temperatures(temperature_room1)
        self.temperature_room2.update_temperatures(temperature_room2)

    def __did_change_view(self, view):
        frame = self.__frames[view]
        frame.tkraise()

if __name__ == "__main__":
    app = MainApp()
    app.run()