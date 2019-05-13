#!/usr/bin/env python3.7

#REF: https://docs.python.org/3/tutorial/controlflow.html#if-statements
#Ref: https://docs.python.org/3/library/stdtypes.html#comparisons

print (1< 2)
print (1> 2)
print(1==1)
print(1==1.0)
print('a' == 'a')
print(3.1 == 'this')  # < and > will cause errors without any base ref.  = will work.
print(3.1 != 'this')
print('a' < 'b')
print ('abc' < 'b')

print(2 in [1,2,3])
print(2 not in [1,2,3])

if True:
    print("was true")

if 1>2:
    print ("this isn't true")
else:
    print("1>2 was false")

name = "patrick"
if len(name) >= 6:
    print ('name is >= 6 char')
elif len(name) == 5:
    print ("name is 5 char")
else:
    print("name is short")
