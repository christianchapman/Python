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
     sub1.append(name1)

f = open (superfile,'r')
print "super file is %s" %(superfile)
for cnt,chris in enumerate(f.readlines()):
#    print " chris is = %s, count is %s\n" %(chris,cnt)
     buffer = chris.split(" ");
     name = buffer[0]
     mac = buffer[1]
     if (mac not in sub1) :
        print "%s %s" %(name,mac)



     
