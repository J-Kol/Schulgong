#!/usr/bin/env python
#coding: utf8

# Schulgong.py
# 16.01.2021 OK

import time
import RPi.GPIO as GPIO

# 
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Pin 22 (GPIO 25) 
# Pin 38 (GPIO 20) 
# Pin 37 (GPIO 26)

Z = int(1)       # interval
numPin = int(37) # pin number

GPIO.setup(numPin, GPIO.OUT)
GPIO.output(numPin, GPIO.LOW)

GPIO.output(numPin, GPIO.HIGH)
time.sleep(Z*1.5)
GPIO.output(numPin, GPIO.LOW)