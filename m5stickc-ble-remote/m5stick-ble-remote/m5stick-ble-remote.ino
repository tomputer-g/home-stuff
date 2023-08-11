#include <M5StickC.h>
#include "Wire.h"
#include <BleKeyboard.h>

BleKeyboard ble("M5StickC");

#define USE_NIMBLE

#define joyI2CAddr 0x54

void setup()
{
  M5.begin();
  M5.Lcd.fillScreen(BLACK);
  M5.Lcd.setTextSize(2);
  Wire.begin(0, 26, 100000UL);
  setCpuFrequencyMhz(80);
  M5.Lcd.printf("aaaa", readButton());
  ble.begin();
}

byte readReg(int address)
{
  Wire.beginTransmission(joyI2CAddr);
  Wire.write(address);
  Wire.endTransmission();
  Wire.requestFrom(joyI2CAddr, 1);
  while (!Wire.available())
    ;
  return Wire.read();
}

void setLED(uint8_t red, uint8_t green, uint8_t blue)
{
  Wire.beginTransmission(joyI2CAddr);
  Wire.write(0x40);
  Wire.write(red);
  Wire.write(green);
  Wire.write(blue);
  Wire.endTransmission();
}

bool readButton()
{
  return readReg(0x30) & 1;
}

int8_t readX()
{
  return readReg(0x20);
}

void flip_page_left()
{
  ble.write(KEY_LEFT_ARROW);
}

void flip_page_right()
{
  ble.write(KEY_RIGHT_ARROW);
}

int state = 0; // 0 = standby, 1 = in right zone, 2 = in left zone (thresh. -100 and +100 respectively)

void loop()
{
  M5.Lcd.fillScreen(BLACK);
  // put your main code here, to run repeatedly:
  M5.update();
  M5.Lcd.setCursor(0, 0);
  int8_t x = readX();

  // State machine
  switch (state)
  {
  case 0:
    if (x < -100)
    {
      state = 2;
      setLED(128, 0, 0);
      flip_page_left();
    }
    else if (x > 100)
    {
      state = 1;
      setLED(0, 0, 128);
      flip_page_right();
    }
    setLED(0, 0, 0);
    break;
  case 1:
    if (x < 90)
    {
      state = 0; // reset
    }
    break;
  case 2:
    if (x > -90)
    {
      state = 0;
    }
    break;
  }

  delay(100);
}
