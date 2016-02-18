#!/usr/bin/python

import serial, struct
import binascii
import time

print "Serial Test"

foo= struct.Struct('<I')
print foo.size



 
ser = serial.Serial(
        port='COM21',
        baudrate= 115200, 
        bytesize=serial.EIGHTBITS,
        timeout=0.0001
        
)


i=0
n=0
t0=0.0
t1=0.0
tMax=0.0
nMax=0
tDiff=0.0
tAv=0.0


##while (ser.readline().strip() != "initialized"):
##        print "uninitialized"  
##
##print "INITIALIZED"
        
while n<1000:

        output= foo.pack(n)
        ser.write(output)
        t0=time.clock()
        print n


        
        incoming_data= foo.unpack(ser.read(foo.size))[0]; 
        print incoming_data
        print n-incoming_data
        t1=time.clock()
        tDiff=t1-t0
        print '{0:.10f}'.format(tDiff)
        if(tDiff)>tMax and n>1:
                tMax= t1-t0
                nMax= n
               
        print ' '
        tAv=tAv+tDiff
                       
        i=i+1

        n=n+1





ser.close()

print tMax
print nMax
print tAv/n

