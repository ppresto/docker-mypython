#!/usr/bin/env python3.7

#Tuples
#Ref: https://docs.python.org/3/library/stdtypes.html#tuple

#Tuple is immutable.  values and length of tuple can't be modified.

point = (2.0, 3.0)
print(point)
point_3d = point + (4.0,)
print (point_3d)
x, y, z = point_3d # assign multiple values
print (x)
print (y)
print (z)

# Format strings are still compatable with Python 2.
# This uses a tuple to substitute the 2 item string 'patrick, presto' into the print function.
print ("My Name is: %s %s" %("Patrick","Presto"))
