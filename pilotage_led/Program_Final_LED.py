#!/usr/bin/env python3
import Jetson.GPIO as GPIO
from time import sleep
import random
import serial 

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#defining the pins as output and input 
#LED Pins
GPIO.setup(23, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
#Bouton Pins
GPIO.setup(22, GPIO.IN)
#Motor Pins
GPIO.setup(15, GPIO.OUT)# Enable pin 
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

#Varriable program 
a=GPIO.input(22)
arduino= serial.Serial("/dev/ttyACM0",9600)


#fonction de chaque color 
def Red_color():
	GPIO.output(19, False)
	GPIO.output(21, False)
	GPIO.output(23, True)
	print ("Red is On")
	sleep(6)
	GPIO.output(19, False)
	GPIO.output(21, False)
	GPIO.output(23, False)
	print ("Red is Off")
	sleep(2)
	print('program is over')
	sleep(2)

def Blue_color():
	GPIO.output(19, False)
	GPIO.output(21, True)
	GPIO.output(23, False)
	print ("Bleu is On")
	sleep(5)
	GPIO.output(19, False)
	GPIO.output(21, False)
	GPIO.output(23, False)
	print ("Bleu is Off")	
	sleep(2)
	print('program is over')
	sleep(2)

def led_blink():
	i=0
	while i<3: 	
		#led blink
		GPIO.output(19, True)
		GPIO.output(21, True)
		GPIO.output(23, False)
		print ("cyan is On")
		sleep(1)
		GPIO.output(19, False)
		GPIO.output(21, False)
		GPIO.output(23, False)
		print ("cyan is Off")
		sleep(2)
		i=i+1
	print('program is over')
	sleep(2)
	
def cyan_color():
	GPIO.output(19, True)
	GPIO.output(21, True)
	GPIO.output(23, False)
	print ("cyan is On")
	sleep(6)
	GPIO.output(19, False)
	GPIO.output(21, False)
	GPIO.output(23, False)
	print ("cyan is Off")	
	sleep(2)
	print('program is over')
	sleep(2)
	
def Green_color():
	GPIO.output(19, True)
	GPIO.output(21, False)
	GPIO.output(23, False)
	print ("Green is On")
	sleep(6)
	GPIO.output(19, False)
	GPIO.output(21, False)
	GPIO.output(23, False)
	print ("Green is Off")	
	sleep(2)
	print('program is over')
	sleep(2)

def Purple_color():
	GPIO.output(19, False)
	GPIO.output(21, True)
	GPIO.output(23, True)
	print ("purple is On")
	sleep(6)
	GPIO.output(19, False)
	GPIO.output(21, False)
	GPIO.output(23, False)
	print ("purple is Off")	
	sleep(2)
	print('program is over')
	sleep(2)

def White_color():
	GPIO.output(19, True)
	GPIO.output(21, True)
	GPIO.output(23, True)
	print ("White is On")
	sleep(6)
	GPIO.output(19, False)
	GPIO.output(21, False)
	GPIO.output(23, False)
	print ("White is Off")	
	sleep(2)
	print('program is over')
	sleep(2)

def Yellow_color():		
	GPIO.output(19, True)
	GPIO.output(21, False)
	GPIO.output(23, True)
	print ("yellow is On")
	sleep(6)
	GPIO.output(19, False)
	GPIO.output(21, False)
	GPIO.output(23, False)
	print ("yellow is Off")
	sleep(2)
	print('program is over')
	sleep(2)

def Motor_control():
	#Motor tourne dans un sens puis l'autre  
	print("motor is On")
	GPIO.output(15, 255)
	GPIO.output(16, True)
	GPIO.output(18, False)
	sleep(4)
	#Motor stop
	print("motor is Off")
	GPIO.output(15, 0)
	GPIO.output(16, False)
	GPIO.output(18, False)
	sleep(4)
	print('program is over')
	
#main pilotage LED 
if a==0:
	while True:
		colorChoise=chr(arduino.read()[0])
		print (colorChoise)
		print ("power On")
		if colorChoise=="B":
			Blue_color()
		elif colorChoise=="R":
			Red_color()
		elif colorChoise=="G":
			Green_color()
		elif colorChoise=="b":
			led_blink()
		elif colorChoise=="C":
			cyan_color()
		elif colorChoise=="Y":
			Yellow_color()
		elif colorChoise=="P":
			Purple_color()
		elif colorChoise=="W":
			White_color()
		elif colorChoise=="M":
			Motor_control()
else:
	print ("power Off Check the power supply")
#fin du program main 
#Reset Des entrée GPIO
GPIO.cleanup()



