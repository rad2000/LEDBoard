#!/usr/bin/python

import led
import time

numleds = 200

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

    dot1 = dot(10, 1, 8, 255, 0, 0)
    list.append(dot1)
    dot2 = dot(80, -2, 5, 0, 255, 0)
    list.append(dot2)
    dot3 = dot(50, 1, 10, 0, 0, 255)
    list.append(dot3)
    dot4 = dot(20, -3, 3, 255, 0, 255)
    list.append(dot4)
    dot5 = dot(70, -1, 3, 0, 255, 255)
    list.append(dot5)
    dot6 = dot(25, 2, 8, 255, 255, 0)
    list.append(dot6)
    dot7 = dot(110, -1, 5, 100, 200, 100)
    list.append(dot7)
    dot8 = dot(108, 3, 10, 0, 0, 100)
    list.append(dot8)
    dot9 = dot(43, -1, 3, 0, 127, 93)
    list.append(dot9)
    dot10 = dot(33, -1, 3, 50, 30, 120)
    list.append(dot10)

    while 1:
        led.setAllLed(0, 0, 0)
        for d in list:
            #led.setLed(d.pos, 0, 0, 0)
            d.pos = d.pos + d.dir
            if d.pos > numleds or d.pos < 0:
                d.dir = d.dir*-1
                d.pos = d.pos + d.dir
            led.setLed(d.pos, d.r, d.g, d.b)
            # now the tail
            #for t in range(0,d.length):
            #    pos = 0
            #    if d.dir < 0:
            #        pos = d.pos + t + 1
            #        if pos > numleds:
            #            pos = numleds - (pos - numleds)
            #    else:
            #        pos = d.pos - (t + 1)
            #        if pos < 0:
            #            pos = abs(pos)
            #    led.setLed(pos, d.r, d.g, d.b)
        led.show()
        led.flush()
        time.sleep(.1)

init()
update()
    
