#!/usr/bin/python

import time
import led

numleds = 150

led.connect()

#for i in range(0, 200):
#    setAllLed('\x00\x00\x00')
#    time.sleep(0.001)
led.setAllLed('\xFF\x00\x00')
time.sleep(0.01)
led.setAllLed('\x00\x00\xFF')
time.sleep(0.01)
led.setAllLed('\x00\xFF\x00')

#led.setLed(50, '\x00\x00\xFF')
#led.show()

