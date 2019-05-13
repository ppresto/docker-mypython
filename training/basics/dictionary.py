#!/usr/bin/env python3.7

#dictionary
#have named indexes.  Keys are immutable, but values can change.

ages = { 'patrick': 42, 'liam': 3, 'lucas': 6 }
print (ages['patrick'])  # 42
ages['liam'] = 4 #update value to 4
print (ages)       # print dictionary

print (ages.get('liam'))  #4
ages.get('patrick') # doesn't return error, just nothing.

print(ages.keys())  # print keys as dict object
print (list(ages.keys()))  # print keys as list
print (list(ages.values()))

ages.pop('patrick')  # safer way to delete things then "del ages['patrick']"
print (ages)

# Create dictionaries in different ways...
weights = dict(patrick=170, liam=27, lucas=40)  # use dict function to create dict object.  Uses tuples
print (weights)

colors = dict([('patrick','green'), ('liam','blue'), ('lucas','red')])
print(colors)
