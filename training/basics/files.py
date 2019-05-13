#!/usr/bin/env python3.7

# open, file object, io module, Bytes objects
# https://docs.python.org/3/library/functions.html#open
# https://docs.python.org/3/glossary.html#term-file-object
# https://docs.python.org/3/library/io.html#io-overview
# https://docs.python.org/3.7/library/stdtypes.html#bytes-objects

my_file = open('xmen.txt', 'w+')  #t for txt mode is implicit.
my_file.write('Beast\n')
my_file.write('Phoenix\n')
my_file.writelines([
    'Cyclops\n',
    'Bishop\n',
    'Nicecrawler\n',
    ])
my_file.close()


my_file = open('xmen.txt', 'r') #t for text mode is implicit.

#auto close file by using "with" stmt
with open('xmen.txt') as my_file:
    print(my_file.read())
    print("I'm reading again")
    print(my_file.read())   #reading curser is already at bottom of file so we wont see anything...
    my_file.seek(0)
    print(my_file.read())  #use seek to reset curser
