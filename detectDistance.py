
#!/usr/bin/python env

import os
import time
import RPi.GPIO as GPIO

def receiveLowVoltage(echoPin):
    return GPIO.LOW == GPIO.input(echoPin)

def receiveHighVoltage(echoPin):
    return GPIO.HIGH == GPIO.input(echoPin)

def initGpioPin(inPin, outPin, pinType):
    GPIO.setmode(pinType)
    GPIO.setup(inPin, GPIO.IN)
    GPIO.setup(outPin, GPIO.OUT)
    GPIO.setup(outPin, GPIO.OUT, initial=GPIO.LOW)

def detectDis(triggerPin, echoPin):

    initGpioPin(echoPin, triggerPin, GPIO.BCM)

    #wait 2 seconds to start get distance
    time.sleep(0.5)
    GPIO.output(triggerPin, GPIO.HIGH)
    time.sleep(0.000015) 
    GPIO.output(triggerPin, GPIO.LOW)

    while receiveLowVoltage(echoPin):
        pass    
    startTime = time.time()

    while receiveHighVoltage(echoPin):
        pass
    endTime = time.time()
    
    interval = endTime - startTime
    distance = interval * 340 / 2

    return distance

def gpioCleanup():
    GPIO.cleanup()


DOOR_OPEN = 1
DOOR_CLOSED = 2
currentDoorStatus = DOOR_CLOSED
doorStatus = DOOR_CLOSED

try:
    while True:
        distance = detectDis(2, 3)
        if distance < 0.95:
            if doorStatus == DOOR_OPEN:
                pass
            else:
                doorStatus = DOOR_OPEN
                print "door is open %f" %distance
                os.system("mplayer /home/pi/python_program/comeOnBaby.m4a < /dev/null > /dev/null 2>1&")
        else:
            if doorStatus == DOOR_CLOSED:
                pass
            else:
                doorStatus = DOOR_CLOSED
                print "door is closed %f" %distance
except KeyboardInterrupt:
    gpioCleanup()
