#! /usr/bin/python
import sys
import os
import pdb

chris = "fuck shit piss"
x = "fu"
cmd = ""
subfile = sys.argv[1]
superfile = sys.argv[2]

sub1 = []
maclst1 = []
sub2 = []
maclst2 = []
f = open (subfile,'r')

for cnt,chris in enumerate(f.readlines()):
#    print " chris is = %s, count is %s\n" %(chris,cnt)
     buffer = chris.split(" ");
            
     chris = chris.strip()
     sub1.append(chris)

for bc in chris:
     txt = " Name =\""+bc

print txt
