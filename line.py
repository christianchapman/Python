#! /usr/bin/python
import sys
import os
import pdb

chris = "fuck shit piss"
x = "fu"
cmd = ""
buf = []
test = sys.argv[1]
f = open (test,'r')
odd = ""
for cnt,chris in enumerate(f.readlines()):
#    print " chris is = %s, count is %s\n" %(chris,cnt)
     chris = chris.strip()
     if ( (cnt != 0)  & ( (cnt % 5) == 0 ) ):
        print buf
        buf = []
        buf.append(chris)
     else:
        buf.append(chris) 
         
    
   #  one = chris.split('.')[0]
   #  two = chris.split('.')[1]
   #  three = chris.split('.')[2]
   #  for x in range(0, 100):
   #       cmd = "ping -c 1 -i 0.3 %s.%s.%s.%s" %(one,two,three,x)
   #       o = os.popen(cmd)
   #       es = o.read();
   #       buffer = es.split("\n");
   #       #pdb.set_trace()
   #       for line in buffer :
   #            if " 0%" in line :
   #                print "%s and result is SUCESS" %(cmd)
   #            if "100%" in line :
   #                print "%s and result is FAILED" %(cmd) 
   #       o.close()
     #     print "ping %s.%s.%s.%s" % (one,two,three,x)
