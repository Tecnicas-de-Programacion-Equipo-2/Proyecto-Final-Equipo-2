from Views.ContainerView import ContainerView
from Views.HomeView import HomeView
from Views.TemperatureView import TemperatureView
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

        self.home = HomeView(self.__master.container, change_view_handler=self.__did_change_view)
        self.temperature = TemperatureView(self.__master.container, change_view_handler=self.__did_change_view,
                                           tap_handler=self.__toggle_did_change)

        self.__frames = {
            View.Home: self.home,
            View.Temperature: self.temperature
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

if __name__ == "__main__":
    app = MainApp()
    app.run()