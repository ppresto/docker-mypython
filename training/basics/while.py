#!/usr/bin/env python3.7

count = 1
while count <= 4:
    print("Looping")
    count += 1

#count odd #'s
count = 0
while count < 10:
    if count %2 == 0:
        count += 1
        continue
    print(f"Counting odd numbers: {count}")  #python 3 uses the f. python2 used "text %s" %count
    count += 1
