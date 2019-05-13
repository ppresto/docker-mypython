#!/usr/bin/env python3.7

import os
import re
import argparse
from glob import glob, iglob

parser = argparse.ArgumentParser()
parser.add_argument("path", help="Input the Root Directory Path to Recursively Check")

args = parser.parse_args()

#for f in glob.iglob(args.path, recursive=True):
#    print (f)
files = glob(args.path + '/**/*.py', recursive=True)
#print (files)


#for path in os.walk(args.path):
#    for f in glob(os.path.join(path[0], '*.py')):
#        print (f)
# Using list comprehension and iglob (iterator gets same value but doesn't store whole list simultaneously)
results = [f for path in os.walk(args.path) for f in iglob(os.path.join(path[0], '*.py'), recursive=True)]

for file in results:
    with open(file) as f:
        body = f.readlines()
        for line in body:
            if re.search('import', line):
                print (f"Line: {body.index(line)+1} - {file} : Found: {line}")
