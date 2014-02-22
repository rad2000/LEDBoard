#!/usr/bin/python

import led
import random
import time
import sys
import threading
import Queue
import time;
from array import *

# Just to test page speed, create a screen full of random colors and draw it as fast as possible

# 140 seems to be the limit at sleep 0.05
numleds = 200

def readInput(inputQueue):
    while 1:
        inputQueue.put(sys.stdin.read(1));

def sendPage():
    print "Sending page"
    arr = array('B')
    for x in range(0,24):
        for y in range(0,8):
            arr.append(page[x][y][0])
            arr.append(page[x][y][1])
            arr.append(page[x][y][2])
    led.setBatch(arr)
    led.show()

def generatepage():
    random.seed()
    arr = array('B')
    for i in range(0,numleds):
        #r = 0 #random.randint(0,255)
        #g = 0 #random.randint(0,255)
        #b = 255 #random.randint(0,255)
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        #led.setLed(i, r, g, b)
        arr.append(r)
        arr.append(g)
        arr.append(b)
    led.setBatch(arr)

def loop():
    delay = 0
    numFrames = 0
    lastTime = 0
    while 1:
        #for i in range(0,1000):
        currentTime = time.clock()
        t = currentTime - lastTime
        if t > 1:
            print "FPS: ", numFrames/t
            numFrames = 0
            lastTime = currentTime
        else:
            numFrames = numFrames + 1
        generatepage()
        #led.flush()
        led.show()
        time.sleep(delay)
        #if not inputQueue.empty():
        #    input = inputQueue.get()
        #    if input == '+' and delay > 0.0001:
        #        print "Faster"
        #        delay = delay/10
        #    elif input == '-' and delay < 10:
        #        print "Slower"
        #        delay = delay*10

page = [[[0,0,0] for col in range(8)] for row in range(24)]

def vertScroll():
    for x in range(1,23):
        for y in range(0,7):
            page[x-1][y] = page[1][y]

def scrollTest():
    lastTime = 0
    while 1:
        currentTime = time.clock()
        t = currentTime - lastTime
        if t > .1:
            lastTime = currentTime
            # Scroll everything
            vertScroll()
            page[23][0] = [255,0,0]
            sendPage()

def map(x, y):
    return x*8+y

    

def init():
    led.connect()
    #global inputQueue
    #inputQueue = Queue.Queue()
    #inputThread = threading.Thread(target=readInput, args=(inputQueue,))
    #inputThread .daemon = True
    #inputThread.start()


init()
loop()
#scrollTest()
