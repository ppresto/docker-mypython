#!/usr/bin/env python3.7

# Open: https://docs.python.org/3/library/functions.html#open
# File Object: https://docs.python.org/3/glossary.html#term-file-object
# IO: https://docs.python.org/3/library/io.html#io-overview

# Open a file
myfile = open('files.txt', 'r')
 # Read it
output = myfile.read()
print(output)
myfile.seek(6)  # bring curser back at index 6
output = myfile.read()
print(output)

myfile.seek(0)  # bring curser back to top of file
for line in myfile:
    # used a custom 'end=""' because we already have a newline char.
    print(line, end="")
myfile.close()

# file mode 'r+' (read, write, update in text mode)
# file mode 'a' appends
# Use 'with' to auto close file.
with open('files.txt', 'r') as base:
    # Copy original file
    with open('new_files.txt', 'w') as w:
        w.write(base.read())
    # Append New Lines
    with open('new_files.txt', 'a') as a:
        a.write("Beast\n")
        a.write("Phoenix\n")

# Print new file contents
with open('new_files.txt', 'r') as r:
    print("....\n")
    for line in r:
        print(line, end="")
