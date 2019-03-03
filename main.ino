#include <Adafruit_NeoPixel.h>
#define PIN 9
#define N_BOXES 9

Adafruit_NeoPixel strip = Adafruit_NeoPixel(
  N_BOXES, PIN, NEO_GRB + NEO_KHZ800
);

class Game;

class Box
{
  public:
  Box()
  {
    _index = 0;
    _color = 0;
  }

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

  int _pin;
  int _index;
  int _color;
  Adafruit_NeoPixel _strip;

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


class Game
{
  Box _boxes[N_BOXES];
  int whoseTurn;

  public:
  Game(Adafruit_NeoPixel strip) {
    _boxes[0] = Box(0, A3, strip);
      // Box(1, 3, strip),
      // Box(2, 4, strip),
      // Box(3, 5, strip),
      // Box(4, 6, strip),
      // Box(5, 7, strip),
      // Box(6, A0, strip),
      // Box(7, A1, strip),
      // Box(8, A2, strip)
  }

  Box getBox(int index) {
    return _boxes[index];
  }
};

Game game = Game(strip);

void setup()
{
  strip.begin();
  game.getBox(0).fill(0);
  // without this, box 0 would just.... turn green. ??
}

void loop()
{
  for (int i=0; i < N_BOXES; i++){
    bool isTurn = game.getBox(i).listen();
    if(isTurn) {
      i = N_BOXES + 1;
    }
  }

  delay(5); // Delay a little bit to improve simulation performance
}