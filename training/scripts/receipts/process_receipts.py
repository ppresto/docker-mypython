#!/usr/bin/env python3.7

# Pre-Req: generate files in ./new using standard Json format with topic, value

import os
import glob
import shutil
import json
import math

try:
    os.mkdir('./processed')
except OSError:
    print(f"./processed dir already exists")

subtotal = 0.0
# Returns list of file paths matching glob.  Will store everything in memory.
#receipts = glob.glob('./new/receipt-[0-9]*.json')
#for path in receipts:

for path in glob.iglob('./new/receipt-[0-9]*.json'):
    with open(path) as f:
        content = json.load(f)
        subtotal += float(content['value'])
    # Split path, and get last item
    #name = path.split("/")[-1]
    #destination = f"./processed/{name}"

    # Use string.replace instead
    destination = path.replace('new', 'processed')
    shutil.move(path, destination)
    print(f"Moved '{path}' to '{destination}'")

# Use print f to truncate to 2 decimal places
#print(f"Receipt subtotal: ${subtotal:.2f}")


# Use Math fuctions from import math
#print(f"Receipt subtotal: ${math.ceil(subtotal)}")
#print(f"Receipt subtotal: ${math.floor(subtotal)}")

# Use round (built-in)
print(f"Receipt subtotal: ${round(subtotal, 2)}")
