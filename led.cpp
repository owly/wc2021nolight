#include <Adafruit_NeoPixel.h>

#define PIXEL_PIN    6    // Digital IO pin connected to the NeoPixels.
#define PIXEL_PIN2    3    // Digital IO pin connected to the NeoPixels.
#define PIXEL_PIN3    4    // Digital IO pin connected to the NeoPixels.

#define PIXEL_COUNT 6

// Parameter 1 = number of pixels in strip,  neopixel stick has 8
// Parameter 2 = pin number (most are valid)
// Parameter 3 = pixel type flags, add together as needed:
//   NEO_RGB     Pixels are wired for RGB bitstream
//   NEO_GRB     Pixels are wired for GRB bitstream, correct for neopixel stick
//   NEO_KHZ400  400 KHz bitstream (e.g. FLORA pixels)
//   NEO_KHZ800  800 KHz bitstream (e.g. High Density LED strip), correct for neopixel stick
Adafruit_NeoPixel strip = Adafruit_NeoPixel(PIXEL_COUNT, PIXEL_PIN, NEO_GRB + NEO_KHZ800);
Adafruit_NeoPixel strip2 = Adafruit_NeoPixel(PIXEL_COUNT, PIXEL_PIN2, NEO_GRB + NEO_KHZ800);
Adafruit_NeoPixel strip3 = Adafruit_NeoPixel(PIXEL_COUNT, PIXEL_PIN3, NEO_GRB + NEO_KHZ800);

long last_0 = millis();
long last_1 = millis();
long last_2 = millis();

void setup(){
  strip.begin();
  strip.show(); // Initialize all pixels to 'off'
  strip2.begin();
  strip2.show(); // Initialize all pixels to 'off'
  strip3.begin();
  strip3.show(); // Initialize all pixels to 'off'
  Serial.begin(9600); //
}
void loop()
{
      int val;
      val=analogRead(0);//Connect the sensor to analog pin 0
      int val1=analogRead(1);//Connect the sensor to analog pin 0
      int val2=analogRead(2);//Connect the sensor to analog pin 0
//      Serial.println(val,DEC);//
      startShow(val, val1, val2);
      delay(50);
}


void startShow(int i, int j, int k) {
  if (j > 15) {
    long elapsedTime = millis() - last_0;
    if (elapsedTime > 500) {
//      Serial.println(j); 
//      Serial.print("j"); 
      Serial.println(0);
      last_0 = millis();
      flash(strip, strip.Color(0, 0, 255));
    }
  }
  if (i > 25) {
//      Serial.println(i); 
//      Serial.print("i"); 
    long elapsedTime2 = millis() - last_2;
    if (elapsedTime2 > 500) {
      Serial.println(2);
      last_2 = millis();
      flash(strip3, strip3.Color(0, 255, 0));  // Red
    }
  }
  if (k > 25) {
    long elapsedTime1 = millis() - last_1;
    if (elapsedTime1 > 500) {
      Serial.println(1);
      last_1 = millis();
      flash(strip2, strip2.Color(255, 0, 0));  // Red
    }
//    Serial.println(k);     
  }
//  Serial.println(i);
//if (j > 11) {
//    Serial.print("J"); //level,DEC);  
//    Serial.println(j); //level,DEC);  
//}
//if (k > 11) {
//    Serial.print("k"); //level,DEC);  
//    Serial.println(k); //level,DEC);  
//    Serial.print("i"); //level,DEC);  
//    Serial.println(i); //level,DEC);  
//}
//  int level = i / 7;
//  if (i < 10) {
//    level = 0;
//  } 
//  else if (i < 20) {
//    level = 1;
//    long num = random(4);
////    Serial.println(num); //level,DEC);
//  } else {
//    level = 2;
////    long num = random(4);
//    Serial.println(random(4)); //level,DEC);
//  }

//  Serial.print("level: ");//
//  Serial.println(level,DEC);//
int s =0;
  switch(s){
    case 0: //showw(0);  
            break;
    case 1: theaterChaseRainbow(127);  
            break;
    case 2: showw(127);
            break;
  }
}

void showw(int bri){
  SnowSparkle(0x10, 0x10, 0x10, 20, 400);
  //theaterChaseRainbow(bri);
}

void setPixel(int Pixel, byte red, byte green, byte blue) {
 #ifdef ADAFRUIT_NEOPIXEL_H 
   // NeoPixel
   strip.setPixelColor(Pixel, strip.Color(red, green, blue));
   strip2.setPixelColor(Pixel, strip.Color(red, green, blue));
   strip3.setPixelColor(Pixel, strip.Color(red, green, blue));
 #endif
 #ifndef ADAFRUIT_NEOPIXEL_H 
   // FastLED
   leds[Pixel].r = red;
   leds[Pixel].g = green;
   leds[Pixel].b = blue;
 #endif
}
void setAll(byte red, byte green, byte blue) {
  for(int i = 0; i < PIXEL_COUNT; i++ ) {
    setPixel(i, red, green, blue); 
  }
  showStrip();
}
void showStrip() {
 #ifdef ADAFRUIT_NEOPIXEL_H 
   // NeoPixel
   strip.show();
   strip2.show();
   strip3.show();
 #endif
 #ifndef ADAFRUIT_NEOPIXEL_H
   // FastLED
   FastLED.show();
 #endif
}
void flash(Adafruit_NeoPixel strip, uint32_t c) {
  for(uint16_t i=0; i<strip.numPixels(); i++) {
    strip.setPixelColor(i, c);
  }
  strip.show();
  delay(100);
  setAllStrip(strip, 255, 255, 255);
}

void setAllStrip(Adafruit_NeoPixel strip, byte red, byte green, byte blue) {
  for(int i = 0; i < PIXEL_COUNT; i++ ) {
    strip.setPixelColor(i, strip.Color(red, green, blue));
//    setPixel(i, red, green, blue); 
  }
  strip.show();
}


void showS(Adafruit_NeoPixel strip) {
 #ifdef ADAFRUIT_NEOPIXEL_H 
   // NeoPixel
   strip.show();
 #endif
 #ifndef ADAFRUIT_NEOPIXEL_H
   // FastLED
   FastLED.show();
 #endif
}

void SnowSparkle(byte red, byte green, byte blue, int SparkleDelay, int SpeedDelay) {
//  setAll(red,green,blue);
  setAll(0,0,0);
 
  int Pixel = random(PIXEL_COUNT);
  setPixel(Pixel,0xff,0xff,0xff);
  showStrip();
  delay(SparkleDelay);
  setPixel(Pixel,red,green,blue);
  showStrip();
  delay(SpeedDelay);
}

//
//    case 0: colorWipe(strip.Color(0, 0, 0), 50);    // Black/off
//            break;
//    case 1: colorWipe(strip.Color(255, 0, 0), 50);  // Red
//            break;
//    case 2: colorWipe(strip.Color(0, 255, 0), 50);  // Green
//            break;
//    case 3: colorWipe(strip.Color(0, 0, 255), 50);  // Blue
//            break;
//    case 4: theaterChase(strip.Color(127, 127, 127), 50); // White
//            break;
//    case 5: theaterChase(strip.Color(127,   0,   0), 50); // Red
//            break;
//    case 6: theaterChase(strip.Color(  0,   0, 127), 50); // Blue
//            break;
//    case 7: rainbow(20);
//            break;
//    case 8: rainbowCycle(20);
//            break;
//    case 9: theaterChaseRainbow(50);
//            break;
//  }
//}

// Fill the dots one after the other with a color
void colorWipe(uint32_t c, uint8_t wait) {
  for(uint16_t i=0; i<strip.numPixels(); i++) {
    strip.setPixelColor(i, c);
    strip.show();
    delay(wait);
  }
}

void rainbow(uint8_t wait) {
  uint16_t i, j;

  for(j=0; j<256; j++) {
    for(i=0; i<strip.numPixels(); i++) {
      strip.setPixelColor(i, Wheel((i+j) & 255));
      strip2.setPixelColor(i, Wheel((i+j) & 255));
      strip3.setPixelColor(i, Wheel((i+j) & 255));
    }
    strip.show();
    delay(wait);
  }
}

// Slightly different, this makes the rainbow equally distributed throughout
void rainbowCycle(uint8_t wait) {
  uint16_t i, j;

  for(j=0; j<256*5; j++) { // 5 cycles of all colors on wheel
    for(i=0; i< strip.numPixels(); i++) {
      strip.setPixelColor(i, Wheel(((i * 256 / strip.numPixels()) + j) & 255));
    }
    strip.show();
    delay(wait);
  }
}

//Theatre-style crawling lights.
void theaterChase(uint32_t c,  int bri = 255) {
  for (int j=0; j<10; j++) {  //do 10 cycles of chasing
    for (int q=0; q < 3; q++) {
      for (int i=0; i < strip.numPixels(); i=i+3) {
        strip.setPixelColor(i+q, c);    //turn every third pixel on
      }
      strip.show();

      delay(11);

      for (int i=0; i < strip.numPixels(); i=i+3) {
        strip.setPixelColor(i+q, 0);        //turn every third pixel off
      }
    }
  }
}

//Theatre-style crawling lights with rainbow effect
void theaterChaseRainbow(int bri) {
  for (int j=0; j < 256; j++) {     // cycle all 256 colors in the wheel
    for (int q=0; q < 3; q++) {
      for (int i=0; i < strip.numPixels(); i=i+3) {
        strip.setPixelColor(i+q, Wheel( (i+j) % 255));    //turn every third pixel on
        strip.setBrightness(bri);
        strip3.setPixelColor(i+q, Wheel( (i+j) % 255));    //turn every third pixel on
        strip3.setBrightness(bri);
        strip2.setPixelColor(i+q, Wheel( (i+j) % 255));    //turn every third pixel on
        strip2.setBrightness(bri);
      }
      strip.show();
      strip3.show();
      strip2.show();

//      delay(11);

//      for (int i=0; i < strip.numPixels(); i=i+3) {
//        strip.setPixelColor(i+q, 0);        //turn every third pixel off
//        strip.setBrightness(bri);
//      }
    }
  }
}

// Input a value 0 to 255 to get a color value.
// The colours are a transition r - g - b - back to r.
uint32_t Wheel(byte WheelPos) {
  WheelPos = 255 - WheelPos;
  if(WheelPos < 85) {
    return strip.Color(255 - WheelPos * 3, 0, WheelPos * 3);
  }
  if(WheelPos < 170) {
    WheelPos -= 85;
    return strip.Color(0, WheelPos * 3, 255 - WheelPos * 3);
  }
  WheelPos -= 170;
  return strip.Color(WheelPos * 3, 255 - WheelPos * 3, 0);
}
//