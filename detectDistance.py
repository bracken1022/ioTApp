#!/usr/bin/python env

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

def detectDis(triggerPin, echoPin, pinType):

    initGpioPin(echoPin, triggerPin, pinType)

    #wait 2 seconds to start get distance
    time.sleep(2)
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

try:
    while True:
        distance = detectDis(2, 3, GPIO.BCM)
        print "distance is %f" % distance
except KeyboardInterrupt:
    gpioCleanup()

