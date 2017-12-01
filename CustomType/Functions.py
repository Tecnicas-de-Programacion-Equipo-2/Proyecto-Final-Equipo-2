from enum import Enum

class Functions(Enum):
    UpdateClockArduino1 = 'update_clock_arduino'
    CloseArduino1 = 'close_arduino'
    UpdateClockArduino2 = 'update_clock_arduino'
    CloseArduino2 = 'close_arduino'
    TurnFan = 'turn_fan'
    FireAlert = 'fire_alert'
    CeaseFireAlert = 'cease_fire_alert'
    IntruderAlert = 'intruder_alert'
    CeaseIntruderAlert = 'cease_intruder_alert'