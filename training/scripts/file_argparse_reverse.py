#!/usr/bin/env python3.7

# https://docs.python.org/3/library/argparse.html

    #import sys
    # Prints full command to script (ex: ./args.py)
    #print(f"First argument {sys.argv[0]}")
    # Print second arg and anything after
    #print(f"Positional arguments {sys.argv[1:]}")
    #print(f"First argument {sys.argv[1]}")

import argparse
import sys

parser = argparse.ArgumentParser(description='Read a file in  reverse')

# Required positional argument
parser.add_argument('filename', help="The file to read")
# Optional arguments
parser.add_argument('--limit','-l', type=int, help='The number of lines to read')
# action - https://docs.python.org/3/library/argparse.html#action
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')

# Returns namespace object with command line args.
args = parser.parse_args()

try:
    f = open(args.filename)
    limit = args.limit

except FileNotFoundError as err:
    print(f"ERROR: {err}")
    sys.exit(1)   #non zero exit code
except:
    print(f"{err}")

else:
    with f:
        # readlines returns a list of lines
        lines = f.readlines()
        # reverse lines
        lines.reverse()

        if args.limit:
            # get slice of list if limit is set
            lines = lines[:args.limit]

        for line in lines:
            # remove newline char and let print add it in for us
            # using -1 step value will print chars from end to start (reverse)
            print(line.strip()[::-1])

finally:
    # print evertime the CLI script is ran.  Useful for cleanup or tasks needed every run.
    pass


# Usage
# ./args_reverseFile.py files.txt
# ./args_reverseFile.py --limit 2 files.txt
