#!/usr/bin/python
import sys
import os

for line1  in sys.stdin:
	#fileName = os.environ['map_input_file']
	#tag = int(fileName[-5:-4])
	line1 = line1.strip()
	#[key1,value1,tag1] = line1.split('\t',2)
	print "%s" %(line1)
