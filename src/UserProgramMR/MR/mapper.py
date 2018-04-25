#!/usr/bin/python
import sys
import json
import os
import ast
for line in sys.stdin:
        #fileName = os.environ['map_input_file']
        #tag = int(fileName[-5:-4])
        line = line.strip()
        my_dict = json.loads(line)
        my_dict = ast.literal_eval(my_dict)
	print "%s"  %(my_dict)
