#!/usr/bin/env python3.7

#Ref: https://docs.python.org/3/library/stdtypes.html#list
#Ref: https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range

import re
# Lists can be changed easily.  Tuples can not.
my_list = [1,2,3,4,5]
print (my_list)
print(my_list[0])
print(my_list[0:]) # print list from beginning to end.
print(my_list[0:-1:1]) # print list excluding last element.
print(my_list[-1])  # print last element of list
print(len(my_list)-1)  #get accurate length
print(my_list[0:2])  #Slicing...  print index 0-1 only
print(my_list[::2])  # Use step value (3rd field).  default is 1 for every item.  2 will give every other value.
print(my_list[::-1])  # Reverse List by using negative step value going backwards.  -1 gives every item.
my_list[0] = "a"  # lists are mutable!
print(my_list)
my_list[0:2] = 'a' # now 1,2 are "a"
print(my_list)
my_list[0:2] = [1,2,3] # add 1,2 back and dont' overwrite 3
print(my_list)
my_list[0:2] = []  # remove items from list, but you should use method instead my_list.remove(0)
print(my_list)
print(my_list.pop()) # returns value, rmoeves from list.  list behanves like a stack (last in, first out)
print(my_list)
print(my_list.pop(0)) # make list behave like a queue (fist in, last out.)
print(my_list)
my_list.append(5)
print(my_list)
my_list.insert(0,3) # insert takes index, value as args.  This will add 3 to the beginning of my_list
my_list += ['a','b'] # my_list += will append values to list
print(my_list)
my_list.remove('a') # remove by value not index.

#####
#      Find
#####
# Find 'b' in list and do something
if 'b' in my_list:
    print(my_list)

# Find 'b' occurences in list
if my_list.count('b') > 0:
    print(f" occures: {my_list.count('b')}, list: {my_list}")

# Findall 'pattern' in a string returns string
my_string = "Patrick is 42, Jessica is 42, Lucas is 6, Liam is 4"
ages = re.findall('\d+', my_string)
print(ages)

# re.match checks first instance
# re.search checks the whole string
for word in my_string.split():
    m = re.search('(\d+)', word)
    if m: print(m.groups())

# re.split builds list from matched patterns in string
print(re.split('\D+', my_string))


#
#  Sort
#

def bubblesort(list):
    for i in range(len(list)-1):
        print(f"{len(list)-1} : {i}")
        for j in range(i):
            print(f"int(j) : {j}")
            if list[j]>list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
                print(f"swapping: {list[j]} with {list[j+1]}")

list = [19,2,31,45,6,11,121,27]
bubblesort(list)
print(list)

test = range(1, 100, 2)
print( [i for i in test if i] )
