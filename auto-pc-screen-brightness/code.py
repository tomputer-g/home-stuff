import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

import time
import board
from analogio import AnalogIn

LDR_in = AnalogIn(board.A3)
# Set up a keyboard device.
kbd = Keyboard(usb_hid.devices)

def send_brightness(brightness: int):
    if brightness == 0:
        kbd.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.ZERO)
    elif brightness == 1:
        kbd.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.ONE)
    elif brightness == 2:
        kbd.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.TWO)
    elif brightness == 3:
        kbd.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.THREE)
    else: 
        kbd.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.FOUR)

def get_LDR_voltage():
    return (LDR_in.value * 3.3) / 65536

while 1:
    print(get_LDR_voltage())
    time.sleep(1)
    
'''
Voltage drops as it gets dimmer.
2.01V - 7:54PM - level 3
1.68V - 8:10PM - level 2
'''