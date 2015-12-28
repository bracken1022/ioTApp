#!/usr/bin/python env

import time
import RPi.GPIO as GPIO


def initPin(inPin, pinType):
    GPIO.setmode(pinType)
    GPIO.setup(inPin, GPIO.IN)


def isLightOn(inPin, pinType):
    initPin(inPin, pinType)

    while True:
        if not GPIO.input(inPin):
            print "light on %f" %time.time()

isLightOn(2, GPIO.BCM)
