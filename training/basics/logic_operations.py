#!/usr/bin/env python3.7

#Ref: https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not

first_name = first or "Jessica"
print(first_name)


print(bool(""))
print(not bool(""))
print('' or 'patrick')  # outputs first true value, if both are true will give first value.

first = ""
last = "Presto"
if first or last:
    print("the user has a part of a name")

first = "Patrick"
last = ""
if first and last:
    print("Full Name Found")  # Nothing prints.
