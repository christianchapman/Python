#!/usr/bin/python

import sys
def printf(format, *args):
    sys.stdout.write(format % args)


# This is an example of print f formating 
fuck = "this is terrible"
shit = "this is shit"
check = " i hate this place ahhhhhh"

bastard = "fuck %-40s cunt %-60s %-40s" % (fuck,shit,check)

print bastard

file_name = "chris"
txt = open(file_name)
lines = txt.readlines()
txt.close()
print lines[0]
jump = "\n\n %s \n\n"  % (lines[44])
print jump
