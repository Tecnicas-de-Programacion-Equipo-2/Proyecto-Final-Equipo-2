from enum import Enum

class Functions(Enum):
    UpdateClock = 'update_clock_arduino'
    Close = 'close_arduino'
    TurnFan = 'turn_fan'
    ChangeBrightness = 'change_led_brightness'
    ReadBrightness = 'read_led_brightness'