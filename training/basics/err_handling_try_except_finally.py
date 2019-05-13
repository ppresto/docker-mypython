#!/usr/bin/env python3.7

# https://docs.python.org/3/reference/compound_stmts.html#the-try-statement

import sys

file_name = 'recipes.txt'

try:
    my_file = open(file_name, 'x')   #If file exists an exception is thrown.  try/except to catch it.
    my_file.write('Meatballs\n')  # setting write mode to bytes not txt (b'Meatballs\n').  throws new exception.
    my_file.close()
except FileExistsError as err:
    print(f"{file_name} file already exists")
    sys.exit(1)   #non zero exit code
except:
    print (f"Unable to write to file")
else:
    print(f"wrote to {file_name}")
finally:
    print("Execution completed")
