from Views.ViewContainer import ViewContainer
#from Views.StartView import StartView
#from Views.ViewOne import ViewOne
#from Views.ViewTwo import ViewTwo
#from CostomeType.View import View
from serial import Serial
from serial.tools import list_ports

class MainApp():

    def __init__(self):
        for port in list_ports.comports():
            print(port.device, port.name, port.description)

        self.__master = ViewContainer()
        self.__arduino = Serial('COM4', 115200)
        self.__master.protocol("WM_DELETE_WINDOW", self.__on_closing)

        #start = StartView(self.__master.container, change_view_hadler=self.__did_change_view)
        #one = ViewOne(self.__master.container, change_view_hadler=self.__did_change_view)
        #two = ViewTwo(self.__master.container, change_view_hadler=self.__did_change_view)

        #self.__frames = {
        #    View.Start: start,
        #    View.One: one,
        #    View.Two: two
        #}

        #self.__master.set_views(self.__frames.values())
        #self.__did_change_view(View.Start)

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
        if temperature >= 28:
            print("******************" * 5)
            print("Encender Ventiladores")
            print("Temperature: ", temperature)

    #def __did_change_view(self, view):
    #    frame = self.__frames[view]
    #    frame.tkraise()

if __name__ == "__main__":
    app = MainApp()
    app.run()