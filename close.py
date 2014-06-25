#!/usr/bin/python

import serial
a = serial.Serial(port='/dev/ttyUSB4', parity='E')

STX = '\x02'
CC = '\x45' # OPEN/CLOSE
PC = '\x30\x00\x00\x00'
ETX = '\x03'
BCC = '\x37\x38'
CMD = STX + CC + PC + ETX + BCC
print('Sending: %s' % repr(CMD))
a.write(CMD)
res = a.read()
print('Received: %s' % repr(res))
