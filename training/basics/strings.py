#!/usr/bin/env python3.7
# Class Name: str
# Strings are immutable.  They can't be modified.  more later...
# Ref:  https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

my_name = "Patrick"
print(my_name + " Presto")
print(my_name) #my_name is unchanged
my_name += " Presto"
print(my_name)  #recreated new string object with "Patrick Presto"


print ("double quote")
print ('single quoted')
print ('''
multi
line
single quote
''')
print ('\nThis is a \nmulti-line\nstring\n')
print ('single' + 'quote')
print ("Ha" * 4)    #multipy to get HaHaHaHa
print ('single'.find('le'))  # find starting index of pattern.  g is at 3.
print ("TeStIng".lower())
print ("Tab\tDelimited")  # escape char tab
print ("New\nLine") # newline
print("Slash\\Character") # Escape the \ to get print a \
print ('\'Single\' quotes')
print ('"Double" quotes')

print ("double".find('s')) #call find method to get substring index.  (-1 not found)
print ("double".find('u')) # index is 2
print ('teStInG'.lower()) # convert to lowercase
print ('testing'.upper()) # convert to uppercase
print ('Capitalize: '+'testing'.capitalize()) # convert first char to capital
print ("HaHaHaHa".count('Ha')) # count substring 'Ha'


mystring = "this is a test"
print(f"reversed: {list(reversed(mystring.split()))}")

if mystring.startswith('this'): print(f"startswith this: {mystring}")
if mystring.split()[0].isalpha(): print(f"isalpha: {mystring.split()[0].upper()}")
if mystring.isnumeric(): print(f"isnumeric: {mystring.upper()}")
if mystring.isdigit(): print(f"isdigit: {mystring.upper()}")
