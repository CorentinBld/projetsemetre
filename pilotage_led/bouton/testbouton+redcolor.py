#!/usr/bin/env python3
import Jetson.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(22, GPIO.IN)
i=0
a=GPIO.input(22)
if a==1:
	print ("power On")
	while i<2:
		#Red color
		GPIO.output(19, True)
		GPIO.output(21, False)
		GPIO.output(23, False)
		print ("Red is On")
		sleep(5)
		GPIO.output(19, False)
		GPIO.output(21, False)
		GPIO.output(23, False)
		print ("Red is Off")
		sleep(1)
		i=i+1	
else:
	print ("power Off Check the power supply")
GPIO.cleanup()



