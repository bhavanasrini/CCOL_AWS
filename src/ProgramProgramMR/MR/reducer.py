#!/usr/bin/python
import math
import sys
import ast
similarity = 0
alphaCategories = 1
betaLocation = 1
key1 = None
key2 = None
input_list = []
def sameCategory(category1,category2):
	#intersectCat = np.intersect1d(category1,category2)
	#unionCat = np.union1d(category1,category2)
	intersectCat = list(set(category1) & set(category2))
	unionCat = list(set(category1) | set(category2))
	return float(len(intersectCat)/len(unionCat))

def localizationFactor(latitude1,longitude1,latitude2,longitude2,cat1,cat2):
	if(latitude1 == 0 or latitude1 == 0  or latitude2 == 0 or latitude2 == 0):
		#catIntersect = np.intersect1d(cat1,cat2)
		intersectCat = list(set(cat1) & set(cat2))
		if(len(intersectCat)==0): return 0
		else:
		     return 0.5	
        radius = 6371
        dlat = math.radians(latitude2-latitude1)
        dlon = math.radians(longitude2-longitude1)
        a = math.sin(dlat/2) * math.sin(dlat/2)+ math.cos(math.radians(latitude1)) * math.cos(math.radians(latitude2)) * math.sin(dlon/2) * math.sin(dlon/2)
        c = 2 * math.atan2(math.sqrt(a),math.sqrt(1-a))
        d = radius * c
	if d > 0: d = 1/d
	else :	  d = 1
	return d 
for line in sys.stdin:
        line = line.strip()
        input_list.append(line)
for line1 in input_list:
	line1 = line1.strip()
	my_dict1 = ast.literal_eval(line1)
	key1 = my_dict1['program_id']
	value1 = my_dict1['latitude']
	value2 = my_dict1['longitude']
	value3 = my_dict1['categories']
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
			key2 = my_dict2['program_id']
			value4 = my_dict2['latitude']
			value5 = my_dict2['longitude']
			value6 = my_dict2['categories']
			tag2 = my_dict2['tag']
			try:
			    key2 = int(key2)
			    tag2 = int(tag2)
			except ValueError:
			    pass    
			if(tag2 == 2):
				if (key1 == key2): similarity = 1
				else :
			     		similarity = float((alphaCategories * sameCategory(value3,value6)) * (betaLocation * localizationFactor(value1,value2,value4,value5,value3,value6))) 
				print'%s\t%s\t%s' %(key1,key2,similarity)
			else:
				pass
	else:
	   pass
