#!/usr/bin/env python3
import Jetson.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#Motor Pins
GPIO.setup(15, GPIO.OUT)# Enable pin 
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

def Motor_control():
	#Motor tourne dans un sens puis l'autre  
	print("motor is On")
	GPIO.output(15, 255)
	GPIO.output(16, True)
	GPIO.output(18, False)
	sleep(6)
	print("motor is On")
	GPIO.output(15, 255)
	GPIO.output(16, False)
	GPIO.output(18, True)
	sleep(6)
	#Motor stop
	print("motor is Off")
	GPIO.output(15, 0)
	GPIO.output(16, False)
	GPIO.output(18, False)
	sleep(2)
	print('program is over')
	


colorChoise=input('Motor:')
print ("power On")
if colorChoise=="motor":
	Motor_control()
#fin du program main 
#Reset Des entrée GPIO
GPIO.cleanup()
