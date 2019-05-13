#!/usr/bin/env python3.7

# zip
numberList = [1, 2, 3]
strList = ['one', 'two', 'three']

print(list(zip(numberList, strList)))  # prints tuple list.  use set...
result = zip(numberList, strList)
resultList = list(result)
x,y = zip(*resultList)
print(f"x = {x} , y = {y}")
