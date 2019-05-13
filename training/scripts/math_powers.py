#!/usr/bin/env python3.7

def power(num, pow):
    if pow == 0:
        return 1
    elif num >= 1:
        return num * (power(num,pow-1))


print (power(2,30))
