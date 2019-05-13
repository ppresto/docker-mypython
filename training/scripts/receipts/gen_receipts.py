#!/usr/bin/env python3.7

# https://docs.python.org/3/library/random.html
# https://docs.python.org/3/library/json.html
# https://docs.python.org/3/library/stdtypes.html#range

# FILE_COUNT=20 python3.7 gen_receipts.property

import random
import json
import os
import re

count = int(os.getenv("FILE_COUNT") or 100)
words = [word.strip() for word in open ('/usr/share/dict/words').readlines()]

for identifier in range(count):
    amount = random.uniform(1.0, 1000)
    content = {
        'topic': random.choice(words),
        # expecting a float, and will support 2 decimal places and put to a string.
        #'value': "%.2f" %amount
        'value': f"{amount:.2f}"
    }
    with open(f'./new/receipt-{identifier}.json', 'w') as f:
        json.dump(content, f)

print(re.match('./new/receipt-[0-9].json','./new/receipt-2.json'))
