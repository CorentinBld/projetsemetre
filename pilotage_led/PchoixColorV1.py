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
a=GPIO.input(22)
i=0
if a==0:
	colorChoise=input('blink,Red,Bleu,Green,cyan,Yellow,Purple,White:')
	print ("power On")
	if colorChoise=="Bleu":
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
		GPIO.cleanup()

	elif colorChoise=="Red":
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
		GPIO.cleanup()

	elif colorChoise=="Green":
		GPIO.output(19, False)
		GPIO.output(21, False)
		GPIO.output(23, True)
		print ("Green is On")
		sleep(6)
		GPIO.output(19, False)
		GPIO.output(21, False)
		GPIO.output(23, False)
		print ("Green is Off")	
		sleep(2)
		print('program is over')
		GPIO.cleanup()	

	elif colorChoise=="blink":
		while i<5: 	
			#led blink
			GPIO.output(19, True)
			GPIO.output(21, True)
			GPIO.output(23, False)
			print ("purple is On")
			sleep(1)
			GPIO.output(19, False)
			GPIO.output(21, False)
			GPIO.output(23, False)
			print ("purple is Off")
			sleep(1)
			i=i+1
		print('program is over')	
		GPIO.cleanup()

	elif colorChoise=="cyan":	
		GPIO.output(19, True)
		GPIO.output(21, True)
		GPIO.output(23, False)
		print ("cyan is On")
		sleep(5)
		GPIO.output(19, False)
		GPIO.output(21, False)
		GPIO.output(23, False)
		print ("cyan is Off")	
		sleep(2)
		print('program is over')
		GPIO.cleanup()
	
	elif colorChoise=="Yellow":
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
		GPIO.cleanup()

	elif colorChoise=="Purple":
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
		GPIO.cleanup()
		
	elif colorChoise=="White":
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
		GPIO.cleanup()
	else :
		print('choose a color thank you')
else:
	print ("power Off Check the power supply")
GPIO.cleanup()
