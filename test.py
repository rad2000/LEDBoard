#!/usr/bin/python

import time
import led

numleds = 200

def doit():
    led.connect()

    max = 200
    for i in range(0, max):
        led.setAllLed(255*(i/max), 255, 255)
        time.sleep(0.01)

    #led.setAllLed(150, 0, 0)
    #time.sleep(.1)

    #led.setAllLed(0, 255, 0)
    #time.sleep(.1)

    #led.setAllLed(0, 0, 100)

    #led.setLed(50, '\x00\x00\xFF')
    #led.show()

doit()
