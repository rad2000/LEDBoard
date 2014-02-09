#!/usr/bin/python

import led

def run():
    led.connect()
    i = 0
    while 1 :
      led.setAllLed(i%255, 255, 255)
      i = i + 1
      if i == 1000 :
        break

run()
