#!/usr/bin/python
from operator import itemgetter
import math
#import numpy as np 
import sys
import json
import ast
similarity = 0
alphaAge = 1
betaDistance = 1
gammaCategories = 1
key1 = None
key2 = None
input_list = []

def ageFactor(age1,age2):
        if(age1 >= age2): AGE = age1/age2
        else:             AGE = age2/age1
        return AGE

def commonUserCategories(category1,category2):
    common = list(set(category1) &  set(category2))
    #common = np.intersect1d(category1,category2)
    return len(common)

def categoriesFactor (category1,category2,Total_Categories):
    return(float(commonUserCategories(category1,category2))/Total_Categories)

def localizationFactor(latitude1,longitude1,latitude2,longitude2):
        radius = 6371
        dlat = math.radians(latitude2-latitude1)
        dlon = math.radians(longitude2-longitude1)
        a = math.sin(dlat/2) * math.sin(dlat/2)+ math.cos(math.radians(latitude1)) * math.cos(math.radians(latitude2)) * math.sin(dlon/2) * math.sin(dlon/2)
        c = 2 * math.atan2(math.sqrt(a),math.sqrt(1-a))
        d = radius * c * 0.621371
	if d > 0: d = 1/d
	else :	  d = 1
	return d 

for line in sys.stdin:
	line = line.strip()
	input_list.append(line)
for line1 in input_list:
	line1 = line1.strip()
	my_dict1 = ast.literal_eval(line1)
	key1 = my_dict1['user_id']
	value1 = my_dict1['age']
	value2 = my_dict1['zipcode']
	value3 = my_dict1['latitude']
	value4 = my_dict1['longitude']
	value5 = my_dict1['Categories']
	value6 = my_dict1['Total Categories']
	tag1 = my_dict1['tag']
	try:
	    key1 = int(key1)
	    tag1 = int(tag1)
	except ValueError:
	    pass    
	if tag1 == 1:
		for line2 in input_list:
			line2 = line2.strip()
			my_dict2 = ast.literal_eval(line2)
			key2 = my_dict2['user_id']
			value7 = my_dict2['age']
			value8 = my_dict2['zipcode']
			value9 = my_dict2['latitude']
			value10 = my_dict2['longitude']
			value11 = my_dict2['Categories']
			value12 = my_dict2['Total Categories']
			tag2 = my_dict2['tag']
			try:
			    key2 = int(key2)
			    tag2 = int(tag2)
			except ValueError:
			    pass    
			if(tag2 == 2):
				if (key1 == key2): similarity = 1
				else :
			     		similarity = float((alphaAge * ageFactor(value1,value7)) * (betaDistance * localizationFactor(value3,value4,value9,value10))*(gammaCategories * categoriesFactor(value5,value11,value12))) 
				print'%s\t%s\t%s' %(key1,key2,similarity)
			else:
				pass
	else:
	   pass
