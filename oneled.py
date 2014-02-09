#!/usr/bin/python

import time
import serial

ser = serial.Serial('/dev/ttyUSB0', 500000)

led = '\x50\x00\xFF\x00'
ser.write(led)
