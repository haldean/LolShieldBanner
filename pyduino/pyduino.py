#!/usr/bin/env python

import serial, glob, sys

class arduino(object):
    def __init__(self):
        self.tty = serial.Serial(self.findserial(), 9600)

    def findserial(self):
        return glob.glob('/dev/ttyUSB*')[0]

    def sendmessage(self, message, uppercase=True):
        if uppercase:
            self.tty.write(message.upper())
        else:
            self.tty.write(message)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        arduino().sendmessage(sys.argv[1])
    else:
        arduino().sendmessage("Everything is under control")
