#! /usr/bin/python
import sys
import os
import pdb

chris = "fzzz szzz pzzzz"
x = "fu"
cmd = ""
test = sys.argv[1]
f = open (test,'r')
odd = ""
for cnt,chris in enumerate(f.readlines()):
#    print " chris is = %s, count is %s\n" %(chris,cnt)
     buffer = chris.split("\t");
     ip = buffer[0]
     ip = ip.strip()
     name = buffer[1]
     name = name.strip()
     if ("roo.iq") not in name :
         if ("ROO.IQ") not in name :
            name = name + ".roo.iq"
     cmd = "dig %s" %(name)
  #   print "command is %s\n" %cmd
     o = os.popen(cmd)
     es = o.read();
     buffer = es.split("\n");
   #       #pdb.set_trace()
     for line in buffer :
           if "A" in line :
               print "found A in %s\n" %line
           if ( ("\tA\t" in line) & (";" not in line) ) :
               print "%s -->  %s --> %s" %(name,ip,line)
           if ( ("SOA" in line) & (";" not in line) ) :
               print "%s --> %s --> %s" %(name,ip,line)
