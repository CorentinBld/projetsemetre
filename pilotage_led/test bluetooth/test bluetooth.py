#!/usr/bin/env python3

import serial
#Serial takes two parameters: serial device and baudrate
ser = serial.Serial('/dev/ttyUSB0', 9600)

data = ser.read()


print(data) 
