# Automatic PC Screen Brightness Changer Project

## Project Overview

Uses a Circuitpython board and a light sensor in conjunction with ClickMonitorDDC v7.2 (found at: https://github.com/chrismah/ClickMonitorDDC7.2) to control the brightness of screens on a Windows PC.

Difficulty: trivial (<1 hr)

## Dependencies

Hardware: QT PY M0 with CircuitPython installed;

+5V -- LDR -- A3 -- R1K -- GND.

Software: VSCode or Thonny with serial monitor.

Packages: adafruit_hid (https://github.com/adafruit/Adafruit_CircuitPython_HID), Neopixel (https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel)

## How it works

The Circuitpython board (I used a [QT PY SAMD21](https://learn.adafruit.com/adafruit-qt-py?view=all) board) is connected with a Light Dependent Resistor (LDR) on a small breadboard, placed in a spot where the lighting of the room is consistent and not easily affected by the screens themselves or other bulbs in the room. The LDR is read periodically by the QT PY, which uses the read voltage and a rough estimate (by my preference) of when to change the screen brightness to decide the target screen brightness.

The ClickMonitorDDC software is configured with hotkeys that translate into brightness commands, which are issued to the monitors via the DDC protocol. The QT PY - when it decides to issue a brightness change - sends one of the hotkeys via USB.

I collected voltage values around the day and mapped them to desired brightness values as calibration.

## What could be improved?

The system is open loop in that:

- If I adjust the brightness manually, the QT PY doesn't know and may abruptly override it.
- Need to manually delay the QT PY upon PC startup, or have a hyperactive period upon power-on that keeps trying to send the same keystrokes over USB. Not elegant

Plus, the voltage values need to be recalibrated whenever the placement of the LDR changes - Hopefully not often.

For a small quick QoL project I opted to not spend more effort on it. This is more than enough compared to manually hitting buttons across two monitors on clunky menus.
