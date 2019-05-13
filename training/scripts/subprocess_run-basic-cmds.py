#!/usr/bin/env python3.7

# https://docs.python.org/3/library/subprocess.html
import subprocess

# proc stdout/stderr returns a byte object.  you can see the 'b' at the start of proc.stdout.
proc = subprocess.run(['ls','-l'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(proc.stdout)

# 0-255 byte chars available in a byte object
#print(bytes([255,0,1]))
# bytes object has decode method to return a string
print(proc.stdout.decode())

# check error return code is 0 and then output.
#newproc = subprocess.run(['cat', 'files.txt'], check=True)

# check error return code is 0, and save output to stdout
newproc = subprocess.run(['cat', 'files.txt'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
print(newproc)
print(newproc.stdout.decode())
