#include "FastLED.h"

// How many leds are in the strip?
#define NUM_LEDS 200
// Data pin that led data will be written out over
#define DATA_PIN 10

// This is an array of leds.  One item for each led in your strip.
CRGB leds[NUM_LEDS];
CRGB buffer;
char tmp[5];
int pos = 0;
int num = 0;
char r, g, b;

void setup() {
  Serial.begin(500000);
  Serial.println("Connected");
  // Initialize LEDs
  FastLED.addLeds<WS2811, DATA_PIN, RGB>(leds, NUM_LEDS);
  setAllLedsTo(CHSV(0, 0, 0));
  FastLED.show();
}

void loop() {
    test2();
}

int size;
int cmd;
void test2() {
    cmd = Serial.read();
    switch(cmd) {
    case 0: // show LEDs!
        FastLED.show();
        break;
    case 1: // set LED
        size = Serial.readBytes(tmp, 4);
	if(size>3) {
	    num = tmp[0];
	    buffer.r = tmp[1];
	    buffer.g = tmp[2];
	    buffer.b = tmp[3];

	    //Serial.write("Got color");
	    //Serial.println(); 
	    setLedTo(num, buffer);
        }
        break;
    }
}


void test1() {
  if(Serial.available()>3) {
    // Each message will have 4 bytes:
    //   1-LED#
    //   2-Red
    //   3-Green
    //   4-Blue
    //int ret = Serial.readBytes(tmp, 4);
    //if(ret == 4) {
    //   int num = tmp[0];
    //   buffer.r = tmp[1];
    //   buffer.g = tmp[2];
    //   buffer.b = tmp[3];
    //} else {
    //  Serial.print("Not enough data");
    // }


//    switch(pos) {
//	case 0:
//            num = Serial.read();
//  	    break;
//          case 1:
//  	    r = Serial.read();
//  	    break;
//          case 2:
//  	    g = Serial.read();
//  	    break;
//          case 3:
//  	    b = Serial.read();
            num = Serial.read();
  	    buffer.r = Serial.read();
  	    buffer.g = Serial.read();
  	    buffer.b = Serial.read();
	    Serial.write("Got color");
	    //Serial.write(buffer.r); 
	    //Serial.write(", ");
	    //Serial.write(buffer.g); 
	    //Serial.write(", ");
	    //Serial.write(buffer.b);
	    Serial.println(); 
	    setLedTo(num, buffer);
	    FastLED.show();
	    //break;
//    }
    pos++;
  }
}

void setLedTo(int led, CRGB rgb) {
  leds[led] = rgb;
}

void setAllLedsTo(CHSV color) {
  for(int i=0; i<NUM_LEDS; i++) {
    leds[i] = color;
  }
}
