#!/usr/bin/python
import datetime
import math
import sys
import ast
def daysFromDate(initialDate):
    return abs((datetime.date.today() - initialDate).days)
def daysFrom(year,month,day):
    initialDate = datetime.date(year,month,day)
    return abs((datetime.date.today() - initialDate).days)
def convDate(enrolldate):
    initialDate = datetime.date(enrolldate[0],enrolldate[1],enrolldate[2])
    return initialDate
def similarity(lenroll,fenroll):
    fenroll = convDate(fenroll)
    lenroll = convDate(lenroll)
    daysSinceFirstEnroll = float(daysFromDate(fenroll))                              
    daysSinceLastEnroll =  float(daysFromDate(lenroll))
    if(daysSinceFirstEnroll==0): return 1
    else:    return (daysSinceLastEnroll/daysSinceFirstEnroll)
for line in sys.stdin:
        line = line.strip()
	my_dict1 = ast.literal_eval(line)
	key1 = my_dict1['user_id']
	value1 = my_dict1['program_id']
	value2 = my_dict1['last_enrollment']
	value3 = my_dict1['first_enrollment']
	value4 = similarity(value2,value3)
	print '%s\t%s\t%s' %(key1,value1,value4)
