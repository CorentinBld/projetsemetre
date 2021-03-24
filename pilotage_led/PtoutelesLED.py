#!/usr/bin/env python3
import Jetson.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#defining the pins as output
GPIO.setup(23, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(22, GPIO.IN)
i=0
t=0
a=GPIO.input(22)
if a==1:
	print ("power On")
	while i<2:
		#Red color
		GPIO.output(19, True)
		GPIO.output(21, False)
		GPIO.output(23, False)
		print ("Red is On")
		sleep(3)
		GPIO.output(19, False)
		GPIO.output(21, False)
		GPIO.output(23, False)
		print ("Red is Off")
		sleep(2)

		#Green color
		GPIO.output(19, False)
		GPIO.output(21, False)
		GPIO.output(23, True)
		print ("Green is On")
		sleep(3)
		GPIO.output(19, False)
		GPIO.output(21, False)
		GPIO.output(23, False)
		print ("Green is Off")		
		sleep(2)
		
		#White color
		GPIO.output(19, True)
		GPIO.output(21, True)
		GPIO.output(23, True)
		print ("White is On")
		sleep(3)
		GPIO.output(19, False)
		GPIO.output(21, False)
		GPIO.output(23, False)
		print ("White is Off")	
		sleep(2)
			
		#Blue color
		GPIO.output(19, False)
		GPIO.output(21, True)
		GPIO.output(23, False)
		print ("Bleu is On")
		sleep(3)
		GPIO.output(19, False)
		GPIO.output(21, False)
		GPIO.output(23, False)
		print ("Bleu is Off")	
		sleep(2)
		#cyan color
		GPIO.output(19, False)
		GPIO.output(21, True)
		GPIO.output(23, True)
		print ("cyan is On")
		sleep(3)
		GPIO.output(19, False)
		GPIO.output(21, False)
		GPIO.output(23, False)
		print ("cyan is Off")	
		sleep(2)
		
		#Purple color
		GPIO.output(19, True)
		GPIO.output(21, True)
		GPIO.output(23, False)
		print ("purple is On")
		sleep(3)
		GPIO.output(19, False)
		GPIO.output(21, False)
		GPIO.output(23, False)
		print ("purple is Off")	
		sleep(2)

		#Yellow color		
		GPIO.output(19, True)
		GPIO.output(21, False)
		GPIO.output(23, True)
		print ("yellow is On")
		sleep(3)
		GPIO.output(19, False)
		GPIO.output(21, False)
		GPIO.output(23, False)
		print ("yellow is Off")	
		sleep(2)

		while t<2:	
			#led blink
			GPIO.output(19, True)
			GPIO.output(21, False)
			GPIO.output(23, False)
			print ("purple is On")
			sleep(1)
			GPIO.output(19, False)
			GPIO.output(21, False)
			GPIO.output(23, False)
			print ("purple is Off")
			sleep(1)
			t=t+1
		i=i+1
	print('program is over')
	GPIO.cleanup()
else:
	print ("power Off Check the power supply")
GPIO.cleanup()
