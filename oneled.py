#!/usr/bin/python

import led

led.connect()
led.setLed(2, 0, 255, 0)
led.flush()
led.show()
