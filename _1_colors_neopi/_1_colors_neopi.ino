// This is a demonstration on how to use an input device to trigger changes on your neo pixels.
// You should wire a momentary push button to connect from ground to a digital IO pin.  When you
// press the button it will change to a new pixel animation.  Note that you need to press the
// button once to start the first animation!

#include <Adafruit_NeoPixel.h>

#define PIXEL_PIN_WIDE    7    // Digital IO pin connected to the NeoPixels.


#define PIXEL_COUNT 5

Adafruit_NeoPixel stripWide = Adafruit_NeoPixel(PIXEL_PIN_WIDE, PIXEL_PIN_WIDE, NEO_GRB + NEO_KHZ800);


void setup() {
  stripWide.begin();
  stripWide.show(); // Initialize all pixels to 'off'
    Serial.begin(9600); //

}

void loop() {
    for(int i=0; i<stripWide.numPixels(); i++) { // For each pixel in strip...
    stripWide.setPixelColor(i, stripWide.Color(128, 128,   0));         //  Set pixel's color (in RAM)
  }
    stripWide.show();                          //  Update strip to match

  delay(500);
    for(int i=0; i<stripWide.numPixels(); i++) { // For each pixel in strip...
    stripWide.setPixelColor(i, stripWide.Color(  0, 255,   0));         //  Set pixel's color (in RAM)
  }
    stripWide.show();                          //  Update strip to match
  delay(500);

}

