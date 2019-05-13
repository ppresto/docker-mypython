#!/usr/bin/env python3.7

# list.  only print green
colors = ['blue','green','red','purple']
for color in colors:
    if color == 'blue':
        continue
    elif color == 'red':
        break
    print(color)


point = (2.1, 3.0, 7)   # Tuple
for value in point:
    print(value)

ages = {'patrick':42, 'liam':4, 'lucas':6}  # Dictionary
for key in ages:  # returns the key.
    print(f"{key} is {ages[key]}")

for letter in "My_string":  # print out each letter vertically.
    print(letter)

list_of_points = [(1,2), (2,3), (3,4)]   #Tuples  sequence of pre defined packaged data points.
for x,y in list_of_points:
    print(f"x: {x}, y: {y}")

for name, age in ages.items():   #items method retursn tuples of Dictionary
    print(f"Person Named: {name}")
    print(f"Age of {age}")
