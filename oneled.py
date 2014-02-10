#!/usr/bin/python

import led


def doit():
    led.connect()
    led.setLed(2, 255, 255, 0)
    led.flush()
    led.show()

doit()
