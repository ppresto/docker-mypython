#!/usr/bin/env python3.7

# https://docs.python.org/3/library/index.html

import time

# FYI: import functions directly allows us to remove "time." from our method call.
# from time import localtime, mktime, strftime

start_time = time.localtime()
#use strftime %X to get current time from users timezone
print(f"Time started at {time.strftime('%X', start_time)}")

# Wait for user to stop timer
input("Press 'Enter' to stop timer")

stop_time = time.localtime()
diff = time.mktime(stop_time) - time.mktime(start_time)

print(f"Time stopped at {time.strftime('%X', stop_time)}")
print(f"Total time: {diff} seconds")
