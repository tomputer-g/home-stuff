# M5StickC BLE Remote

### Project Overview

Using a M5StickC (ESP32-based embedded systems product) and a MiniJoyC (Joystick/Battery/LED module) together, this project is designed so that the user's motions on the Joystick are reflected via a Bluetooth connection to the computer connected.

Current usages include:

* Flipping pages on the Kindle PC application

### References

I2C register map: https://static-cdn.m5stack.com/resource/docs/products/hat/MiniJoyC/arduinoCase-1672293992601%E6%97%A0%E6%A0%87%E9%A2%981.png

Using library BleKeyboard: https://github.com/T-vK/ESP32-BLE-Keyboard/blob/master/BleKeyboard.cpp

Example of BleKeyboard presenter using M5StickC: https://github.com/tanakamasayuki/M5StickC-examples/blob/master/M5StickcBluetoothPresenter/M5StickcBluetoothPresenter.ino

