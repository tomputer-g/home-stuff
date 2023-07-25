import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
kbd = Keyboard(usb_hid.devices) #Pretend we're a keyboard

import time
import board
from analogio import AnalogIn
LDR_in = AnalogIn(board.A3) #Light Dependent Resistor in a voltage divider formation over A3

import neopixel
led = neopixel.NeoPixel(board.NEOPIXEL, 1) # To signify status
led.brightness = 0.3

THRESHOLDS = [0.6, 1.1, 1.5, 1.8] # Simple dividers for five brightness options
DETECT_PERIOD_SEC = 60 # Period of time between scan/sets

# Hotkeys set in ClickMonitorDDC
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

def LDR_to_desired_brightness(voltage: float):
    if voltage < THRESHOLDS[0]:
        return 0
    elif voltage < THRESHOLDS[1]:
        return 1
    elif voltage < THRESHOLDS[2]:
        return 2
    elif voltage < THRESHOLDS[3]:
        return 3
    else:
        return 4

while 1:
    ldr_v = get_LDR_voltage()
    print(ldr_v)
    brightness = LDR_to_desired_brightness(ldr_v)
    send_brightness(brightness)
    led[0] = (0, 25, 0)
    time.sleep(0.5)
    led[0] = (0,0,0)
    time.sleep(DETECT_PERIOD_SEC - 0.5)
    
'''
Voltage drops as it gets dimmer.
2.01V - 7:54PM - level 3
1.68V - 8:10PM - level 2
1.40V - 8:24PM - level 2
0.94V - 8:25PM, partial curtains, table lamp, lights - level 1
0.40V - 8:25PM, table lamp, lights, curtains - level 0
'''