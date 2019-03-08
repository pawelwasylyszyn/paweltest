#!/usr/bin/python

import struct

# devOffsets.dirtyGranularity, combSizeInLbs and flags are UINT32, the rest is UINT64
keys = [ 'sigStart', 'devVersion', 'tgtId', 'devId', 'devOffsets.combsMapOffset', 'devOffsets.teethMapOffset', 'devOffsets.activeBmOffset', 'devOffsets.rebuildBmOffset', 'devOffsets.freeSpaceOffset','devOffsets.teethOffset', 'devOffsets.devSizeInLbs', 'devOffsets.maxNumOfCombs', 'devOffsets.numOfTeeth', 'devOffsets.dirtyGranularity', 'combSizeInLbs', 'sigEnd', 'flags' ]

def readSDSDev(fname,debug=False):
    mydict = {}
    try:
        myf = open(fname,'rb')
        myf.seek(32768)
    except Exception as e:
        print ("Couldn't open file: '" + str(fname) + "', error: " + repr(e))
        return {}

    for i in keys:
        if debug:
                print i
        if (i in ( "devOffsets.dirtyGranularity" , "combSizeInLbs" , "flags") ):
                try:
                        hx = myf.read(4)
# struct.unpack always returns a tuple, not a single value
                        (bt) = struct.unpack("I", hx)
                except Exception as e:
                        print ("Couldn't read file: '" + str(fname) + "', error: " + repr(e))
        else:
                try:
                        hx = myf.read(8)
                        (bt) = struct.unpack("Q", hx)
                except Exception as e:
                        print ("Couldn't read file: '" + str(fname) + "', error: " + repr(e))
        mydict[i] = bt[0]
    return mydict


abc = readSDSDev("/dev/sdb", False)
for (k,v) in abc.items():
        print (k.ljust(27) + " = " + str(v) + " (" + str(hex(v)) + ")" )

