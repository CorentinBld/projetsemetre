#!/usr/bin/env python3
import Jetson.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(22, GPIO.IN)

a=GPIO.input(22)
if a==1:
	print ("power On")
else:
	print ("power Off Check the power supply")
GPIO.cleanup()

