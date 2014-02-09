#!/usr/bin/python

import time
import serial

ser = 0

numleds = 150

def show():
    ser.write(chr(0))

def setLed( num, str ):
    output = chr(1) + chr(num)+str;
    ser.write(output)

def setAllLed( str ):
    for led in range(0, numleds):
        setLed(led, str)
    ser.flush()
    show()

def connect():
    global ser
    ser = serial.Serial('/dev/ttyUSB0', 500000)

def monitor():
    while 1 : ser.readline()
