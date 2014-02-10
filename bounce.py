#!/usr/bin/python

import led
import time

numleds = 127

class dot:
    def __init__(self, pos, dir, length, r, g, b):
       self.pos = pos
       self.dir = dir
       self.length = length
       self.r = r
       self.g = g
       self.b = b


def init():
    led.connect()

def update():
    list = []

    dot1 = dot(10, 2, 10, 255, 0, 0)
    list.append(dot1)
    dot2 = dot(80, -3, 5, 0, 255, 0)
    list.append(dot2)

    while 1:
        for d in list:
            led.setLed(d.pos, 0, 0, 0)
            d.pos = d.pos + d.dir
            if d.pos > numleds or d.pos < 0:
                d.dir = d.dir*-1
                d.pos = d.pos + d.dir
            led.setLed(d.pos, d.r, d.g, d.b)
        led.show()
        led.flush()
        time.sleep(.05)

init()
update()
    
