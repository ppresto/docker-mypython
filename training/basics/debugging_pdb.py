#!/usr/bin/env python3.7

# Run this script from command line and get break point.  This is interactive so we can get variable values.
# ex: values, output_values, index
# we can run pdb commands like 'n' for next instruction
# ex: h, help cont, help next, list, n
#
# optional usage:
# we can use pdb with break command at runtime without adding to script.
# run your script like this... 'python3.7 -m pdb my.py'
# list your script, 'll'
# add break point at line 5 with a condition using this command 'break 5, index == 5'
# 'll'
import pdb

def map(func, values):
    output_values = []
    index = 0
    while index < len(values):
        pdb.set_trace()   # set trace inside the loop
        output_values.append(func(values[index]))
        index += 1
    return output_values

def add_one(val):
    return val + 1

print(map(add_one, list(range(10))))
