#!/usr/bin/python

import time
import serial


def show():
    ser.write(chr(0))

def setLed( num, str ):
    output = chr(1) + chr(num)+str;
    ser.write(output)

def setAllLed( str ):
    for led in range(0, numleds):
        setLed(led, str)
    show()

ser = serial.Serial('/dev/ttyUSB0', 500000)
numleds = 100

#for i in range(0, 200):
#    setAllLed('\x00\x00\x00')
#    time.sleep(0.001)
setAllLed('\xFF\x00\x00')
time.sleep(0.01)
setAllLed('\x00\xFF\x00')
time.sleep(0.01)
setAllLed('\x00\x00\xFF')
