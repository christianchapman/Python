#! /usr/bin/python
import sys
import os
import pdb
import re

### use xxx.py <subfile> <superfile>

subfile = sys.argv[1]
name_data = []
name_list =[]
k = 0
i = 0
f = open (subfile,'r')
j = 0
whole_file = f.readlines()
file_len = len(whole_file)
for k in whole_file:
   if "return" in k :
      j = k.split(";")
      print "the string is %s\n" %(j)
      for i in j :
         print "%s\n" %(i)
         if "." in i:
          x = re.sub(":[0-9]{1,4}", "", i)
          y = re.sub ("PROXY ","",x)
          z = re.sub ("return ","",y)
          print " it has been cleaned %s\n" %(z)


