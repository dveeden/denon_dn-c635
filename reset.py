#!/usr/bin/python

import serial
a = serial.Serial(port='/dev/ttyUSB4', parity='E')

STX = '\x02'
CC = '\x20' # RESET
PC = '\x00\x00\x00\x00'
ETX = '\x03'
BCC = '\x32\x33'
CMD = STX + CC + PC + ETX + BCC
print('Sending: %s' % repr(CMD))
a.write(CMD)
res = a.read()
print('Received: %s' % repr(res))
