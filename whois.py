#! /usr/bin/python

import sys
import os
import pdb
import re

fname = sys.argv[1]

d = re.search(r'(\.[0-9]{1,3})',fname)

if (d):
# pdb.set_trace()
 line = fname
 ip = "whois "+line
 look = os.popen(ip).readlines()
 for entry in look :
  print("---->%-20s %-20s" % (line.rstrip('\n'),entry.rstrip('\n')))
 dig = "dig -x" +line
 look = os.popen(dig).readlines()
 for entry in look :
   print("######## DIG -X  %-20s %-20s " % ( line.rstrip('\n'), entry.rstrip('\n') ) )
else :
 txt = open(fname)
 for line in txt:
 #   pdb.set_trace()
    ip = "whois "+line
    look = os.popen(ip).readlines()
    for entry in look :
      print("---->%-20s %-20s" % (line.rstrip('\n'),entry.rstrip('\n')))
