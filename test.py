#!/usr/bin/python

import sys
def printf(format, *args):
    sys.stdout.write(format % args)


# This is an example of print f formating 
fzz = "this is f"
szz = "this is s"
check = " this is c"

b= "fzz %-40s czz %-60s %-40s" % (fzz,szz,check)

print b

file_name = "chris"
txt = open(file_name)
lines = txt.readlines()
txt.close()
print lines[0]
jump = "\n\n %s \n\n"  % (lines[44])
print jump
