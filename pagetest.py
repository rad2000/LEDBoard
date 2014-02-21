#!/usr/bin/python

import led
import random
import time
from array import *

# Just to test page speed, create a screen full of random colors and draw it as fast as possible

# 140 seems to be the limit at sleep 0.05
numleds = 200

def generatepage():
    random.seed()
    arr = array('B')
    for i in range(0,numleds):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        #led.setLed(i, r, g, b)
        arr.append(r)
        arr.append(g)
        arr.append(b)
    led.setBatch(arr)

def loop():
    while 1:
        generatepage()
        led.flush()
        led.show()
        time.sleep(1)

def init():
    led.connect()

init()
loop()
