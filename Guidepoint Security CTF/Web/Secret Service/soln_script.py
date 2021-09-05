#!/usr/bin/python
# Python 3 implementation to find
# the colour where the mod is equal to zero
 
def findColour() :
    n = 2040			#sum of the date
    m = 8			#number of colours  
    while n % m != 0:
    	m = m- 1
    print (m)
print(findColour())
     

