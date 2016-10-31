
#!/usr/bin/python

# cut.py <filename> <column to display>

import sys

filename = sys.argv[1]
col = sys.argv[2]
#print "filename is"+filename
cap = open (filename)
buf = cap.readlines()
for i in buf :
  j = i.split()
  print j[int(col)]
