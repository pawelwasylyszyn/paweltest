#!/usr/bin/python

import struct
import argparse


# devOffsets.dirtyGranularity, combSizeInLbs and flags are UINT32, the rest is UINT64
keys = [ 'sigStart', 'devVersion', 'tgtId', 'devId', 'devOffsets.combsMapOffset', 'devOffsets.teethMapOffset', 'devOffsets.activeBmOffset', 'devOffsets.rebuildBmOffset', 'devOffsets.freeSpaceOffset','devOffsets.teethOffset', 'devOffsets.devSizeInLbs', 'devOffsets.maxNumOfCombs', 'devOffsets.numOfTeeth', 'devOffsets.dirtyGranularity', 'combSizeInLbs', 'sigEnd', 'flags' ]

def readSDSDev(fname,debug):
    mydict = {}
    try:
        myf = open(fname,'rb')
        myf.seek(32768)
    except Exception as e:
        print ("Couldn't open file: '" + str(fname) + "', error: " + repr(e))
        return {}

    for i in keys:
        if debug:
                print "Reading: " + i
        if (i in ( "devOffsets.dirtyGranularity" , "combSizeInLbs" , "flags") ):
                try:
                        hx = myf.read(4)
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


parser = argparse.ArgumentParser(description='Provide a disk name (i.e. /dev/sdb) [-d <debug>]')
parser.add_argument("-d", "--debug")
parser.add_argument('disk')

args = parser.parse_args()
print args

abc = readSDSDev(args.disk, True)
for (k,v) in abc.items():
        print (k.ljust(27) + " = " + str(v) + " (" + str(hex(v)) + ")" )

