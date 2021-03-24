#!/usr/bin/env python3
#defining the Jetson's pins as Input / Output
import Jetson.GPIO as GPIO

#importing the library for delaying command.
from time import sleep 

#used for GPIO numbering
GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.OUT)
#closing the warnings when you are compiling the code
GPIO.setwarnings(False)

RUNNING = True

#defining the pins
green = 23
red =19
blue = 21
#defining the pins as output
GPIO.setup(red,GPIO.OUT) 
GPIO.setup(green,GPIO.OUT)
GPIO.setup(blue,GPIO.OUT)

#init
GPIO.OUTPUT(red,GPIO.LOW)  
GPIO.OUTPUT(green,GPIO.LOW)
GPIO.OUTPUT(blue,GPIO.LOW)

while RUNNING: 
#Red color
	GPIO.OUTPUT(red,GPIO.HIGH)  
	GPIO.OUTPUT(green,GPIO.LOW)
	GPIO.OUTPUT(blue,GPIO.LOW)
	time.sleep(2)
#Green color		
	GPIO.OUTPUT(red,GPIO.LOW)  
	GPIO.OUTPUT(green,GPIO.HIGH)
	GPIO.OUTPUT(blue,GPIO.LOW)
	time.sleep(2)
#White color
	GPIO.OUTPUT(red,GPIO.HIGH)  
	GPIO.OUTPUT(green,GPIO.HIGH)
	GPIO.OUTPUT(blue,GPIO.HIGH)
	time.sleep(2)
#Blue color
	GPIO.OUTPUT(red,GPIO.LOW)  
	GPIO.OUTPUT(green,GPIO.LOW)
	GPIO.OUTPUT(blue,GPIO.HIGH)
	time.sleep(2)
#cyan color
	GPIO.OUTPUT(red,GPIO.LOW)  
	GPIO.OUTPUT(green,GPIO.HIGH)
	GPIO.OUTPUT(blue,GPIO.HIGH)
	time.sleep(2)
#Purple color
	GPIO.OUTPUT(red,GPIO.HIGH)  
	GPIO.OUTPUT(green,GPIO.LOW)
	GPIO.OUTPUT(blue,GPIO.HIGH)
	time.sleep(2)
#Yellow color
	GPIO.OUTPUT(red,GPIO.HIGH)  
	GPIO.OUTPUT(green,GPIO.LOW)
	GPIO.OUTPUT(blue,GPIO.HIGH)
	time.sleep(2)

#led blink
	GPIO.OUTPUT(red,GPIO.HIGH)  
	GPIO.OUTPUT(green,GPIO.LOW)
	GPIO.OUTPUT(blue,GPIO.HIGH)
	time.sleep(1)
#led Switch OFF	
	GPIO.OUTPUT(red,GPIO.LOW)  
	GPIO.OUTPUT(green,GPIO.LOW)
	GPIO.OUTPUT(blue,GPIO.LOW)
	time.sleep(1)
#led Switch ON
	GPIO.OUTPUT(red,GPIO.HIGH)  
	GPIO.OUTPUT(green,GPIO.LOW)
	GPIO.OUTPUT(blue,GPIO.HIGH)
	time.sleep(1)
	
