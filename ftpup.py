#!/usr/bin/env python
import serial,time   # Importing required modules
port = serial.Serial(baudrate=9600, port='Path of Device(For Example </dev/ttyUSB0>)', timeout=1)
port.flush()
port.write('''AT+CGATT\r''')
time.sleep(10)
port.write("AT+CIICR\r")
time.sleep(10)
port.write("AT+CIFSR\r")
time.sleep(10)
port.write("AT+FTPCID=1\r")
time.sleep(10)

port.write("AT+SAPBR=1,1\r")
time.sleep(10)
port.write("AT+FTPSERV=\"ftpserveraddress\"\r")
time.sleep(10)
port.write("AT+FTPUN=\"username\"\r")
time.sleep(10)
port.write("AT+FTPPW=\"userpassword\"\r")
time.sleep(10)

port.write("AT+FTPPUTNAME=\"filename\"\r")
time.sleep(10)
port.write("AT+FTPPUTPATH=\"/\"\r")
time.sleep(10)

port.write("AT+FTPPUT=1\r")
time.sleep(10)
port.write("AT+FTPPUT=2,100\r")
time.sleep(10)

port.write("Write A Message\r")
time.sleep(10)
port.write("AT+FTPPUT=2,0\r")
time.sleep(10)
while(1):      # just For Reading  Response From The Device

  print port.read(10)

