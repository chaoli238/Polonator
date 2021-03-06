#! /usr/bin/env python
"""\
Scan for serial ports. Linux specific variant that also includes USB/Serial
adapters.

Part of pySerial (http://pyserial.sf.net)
(C) 2009 <cliechti@gmx.net>
"""

import serial
import glob

"""
     The Port mapping is as follows
     
"""

def getSerialPortList():
     """
          returns a list of serial ports 
          scan for available ports. return a list of device names.
     """
     return glob.glob('/dev/ttyS*') + glob.glob('/dev/ttyUSB*')

if __name__=='__main__':
    print "Found ports:"
    for name in getSerialPortList():
        print name
        
        
