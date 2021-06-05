// This is a demonstration on how to use an input device to trigger changes on your neo pixels.
// You should wire a momentary push button to connect from ground to a digital IO pin.  When you
// press the button it will change to a new pixel animation.  Note that you need to press the
// button once to start the first animation!

#include <Adafruit_NeoPixel.h>

#define PIXEL_PIN    6    // Digital IO pin connected to the NeoPixels.
#define PIXEL_PIN2    5    // Digital IO pin connected to the NeoPixels.
#define PIXEL_PIN3    4    // Digital IO pin connected to the NeoPixels.
#define PIXEL_PIN4    7    // Digital IO pin connected to the NeoPixels.
#define PIXEL_PIN7    7    // Digital IO pin connected to the NeoPixels.


#define PIXEL_COUNT 5

Adafruit_NeoPixel strip = Adafruit_NeoPixel(22, PIXEL_PIN, NEO_GRB + NEO_KHZ800);
Adafruit_NeoPixel strip2 = Adafruit_NeoPixel(22, PIXEL_PIN2, NEO_GRB + NEO_KHZ800);
Adafruit_NeoPixel strip3 = Adafruit_NeoPixel(77, PIXEL_PIN3, NEO_GRB + NEO_KHZ800);
Adafruit_NeoPixel strip4 = Adafruit_NeoPixel(22 , PIXEL_PIN4, NEO_GRB + NEO_KHZ800);

uint32_t RED = strip.Color(255, 0, 0);
uint32_t ORANGE = strip.Color(255, 30, 0);
uint32_t YELLOW = strip.Color(128, 255, 55);
uint32_t GREEN = strip.Color(0, 255, 0);
uint32_t BLUE = strip.Color(11,222,222);
uint32_t PURPLE = strip.Color(249,189,255);


void setup() {
  strip.begin();
  strip.show(); // Initialize all pixels to 'off'
  strip2.begin();
  strip2.show(); // Initialize all pixels to 'off'
  strip3.begin();
  strip3.show(); // Initialize all pixels to 'off'
  strip4.begin();
  strip4.show(); // Initialize all pixels to 'off'

        Serial.print("1:"); 
        Serial.print(strip.numPixels()); 
        Serial.print("2:"); 
        Serial.print(strip2.numPixels()); 
        Serial.print("3:"); 
        Serial.print(strip3.numPixels()); 
        Serial.print("4:"); 
        Serial.print(strip4.numPixels()); 
    Serial.begin(9600); //

}

void loop() {
    for(int i=0; i<strip.numPixels(); i++) { // For each pixel in strip...
      strip.setPixelColor(i, RED);         //  Set pixel's color (in RAM)
    }
    for(int i=0; i<strip2.numPixels(); i++) { // For each pixel in strip...
      strip2.setPixelColor(i, YELLOW);         //  Set pixel's color (in RAM)
    }
    for(int i=0; i<strip3.numPixels(); i++) { // For each pixel in strip...
      strip3.setPixelColor(i, BLUE);         //  Set pixel's color (in RAM)
    }
    for(int i=0; i<strip4.numPixels(); i++) { // For each pixel in strip...
      strip4.setPixelColor(i, PURPLE);         //  Set pixel's color (in RAM)
    }
    strip.show();                          //  Update strip to match
    strip2.show();                          //  Update strip to match
    strip3.show();                          //  Update strip to match
    strip4.show();                          //  Update strip to match

  delay(500);
//    for(int i=0; i<strip.numPixels(); i++) { // For each pixel in strip...
//    strip.setPixelColor(i, strip.Color(255,   0,   0));         //  Set pixel's color (in RAM)
//    }
//    for(int i=0; i<strip2.numPixels(); i++) { // For each pixel in strip...
//    strip2.setPixelColor(i, strip.Color(  0, 255,   0));         //  Set pixel's color (in RAM)
//    }
//    for(int i=0; i<strip3.numPixels(); i++) { // For each pixel in strip...
//    strip3.setPixelColor(i, strip.Color(  0,   0, 255));         //  Set pixel's color (in RAM)
//    }
//    for(int i=0; i<strip4.numPixels(); i++) { // For each pixel in strip...
//    strip4.setPixelColor(i, strip.Color(  0,   0,   0, 255));         //  Set pixel's color (in RAM)
//  }
    strip.clear();                          //  Update strip to match
    strip2.clear();                          //  Update strip to match
    strip3.clear();                          //  Update strip to match
    strip4.clear();                          //  Update strip to match
    strip.show();                          //  Update strip to match
    strip2.show();                          //  Update strip to match
    strip3.show();                          //  Update strip to match
    strip4.show();                          //  Update strip to match
  delay(500);

}

