#!/usr/bin/python

import time
import serial
from array import *

ser = 0

numleds = 200


def show():
    ser.write(chr(0))

def setLed( num, r, g, b ):
    arr = array('B')
    arr.append(1)
    arr.append(num)
    arr.append(r)
    arr.append(g)
    arr.append(b)
    ser.write(arr.tostring())

def setAllLed( r, g, b ):
    arr = array('B')
    arr.append(2)
    arr.append(r)
    arr.append(g)
    arr.append(b)
    #for led in range(0, numleds):
    #    setLed(led, r, g, b)
    #ser.flush()
    ser.write(arr.tostring())
    show()


def flush():
    ser.flush();



def connect():
    global ser
    ser = serial.Serial('/dev/ttyUSB0', 1000000)

def monitor():
    while 1 : ser.readline()
