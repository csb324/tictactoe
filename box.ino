#include <Adafruit_NeoPixel.h>

class Box
{
  int _pin;
  int _index;
  int _color;
  Adafruit_NeoPixel _strip;

  public:
  Box(int index, int pin, Adafruit_NeoPixel strip)
  {
    _index = index;
    _color = 0;
    _pin = pin;
    _strip = strip;
    pinMode(pin, INPUT);
  }

  void fill(int color)
  {
    _color = color;
    this->show();
  }
  void reset()
  {
    _color = 0;
    this->show();
  }

  bool listen()
  {
    if(_color == 0) {
      int value_from_pin = digitalRead(_pin);
      if (value_from_pin == 1) {
        this->fill(1);
        _strip.show();
        return true;
      }
    }
    return false;
  }

  int getColor() {
    return _color;
  }

  private:
  void show()
  {
    if (_color == 2) {
      _strip.setPixelColor(_index, 255, 0, 255);
    }
    if (_color == 1) {
      _strip.setPixelColor(_index, 255, 255, 0);
    }
    if (_color == 0) {
      _strip.setPixelColor(_index, 0, 0, 0);
    }
  }
};
