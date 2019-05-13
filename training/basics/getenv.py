#!/usr/bin/env python3.7

# https://docs.python.org/3/library/os.html
# https://docs.python.org/3/library/os.html#os.environ
# https://docs.python.org/3/library/os.html#os.getenv

import os

stage = os.getenv('STAGE','dev').upper()  # default env is Dev if nothing is set in Env.
output = f"We're running in {stage}"

if stage.startswith('PROD'):
    output = "DANGER!!!  - " + output
print (output)
