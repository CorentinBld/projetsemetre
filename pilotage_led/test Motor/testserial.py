#!/usr/bin/env python3
import Jetson.GPIO as GPIO
from time import sleep
import serial 
arduino= serial.Serial("/dev/ttyACM0",9600)
while True:
	reception=chr(arduino.read()[0])
	print (reception)
	
