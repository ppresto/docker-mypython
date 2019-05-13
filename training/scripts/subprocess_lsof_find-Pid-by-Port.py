#!/usr/bin/env python3.7

import argparse
import subprocess
import os
import sys

parser = argparse.ArgumentParser("description = free up used port #")
parser.add_argument('port', type=int, help="enter port #")

args = parser.parse_args()

try:
    processes = subprocess.run(['lsof', '-n','-i4TCP:' + str(args.port)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
except subprocess.CalledProcessError as err:
    print("Error")
    sys.exit(1)
for line in processes.stdout.splitlines():
    if "LIST" in line.decode():
        print(line)
        pid = int(line.split()[1])
        os.kill(pid, 9)
        print (f"killed process: {pid}")
    else:
        print(f"No process listening on port: {args.port}")
        sys.exit(1)
if "LIST" not in processes.stdout.decode():
    print(f"No process listening on the port: {args.port}")
    sys.exit(1)
