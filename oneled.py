#!/usr/bin/python

import led

def doit():
    led.connect()
    led.setLed(20, 255, 0, 0)
    led.flush()
    led.show()

doit()
