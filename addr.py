#! /usr/bin/python
import sys
import os
import pdb
import glob
import re
path="/export/home/nms/bulk_config/cisco/*.load"
#pdb.set_trace()
for file in glob.glob(path):
    with open(file,'r') as f:
 #    pdb.set_trace()
     for chris in f.readlines():
       if re.search(r"^ ip address [1-9]",chris): 
   #    print "this is %s" %(chris)
  #      pdb.set_trace()
        subnet = chris.split(' ')[3]
        mask = chris.split(' ')[4]
        mask = mask.rstrip("\r\n")
        filename = file.split("/")[6]
     #   pdb.set_trace()
        print "%s %s %s" %(filename,subnet,mask)
