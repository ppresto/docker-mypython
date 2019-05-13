#!/usr/bin/env python3.7

# https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

# get words dictionary
# debian: apt-get install --reinstall wamerica
# centos: yum install words

import argparse
from collections import Counter
from itertools import permutations
import re, string

parser = argparse.ArgumentParser(description="Search for words including partial word")
parser.add_argument('snippet', help='partial or complete string to search for in words')
parser.add_argument('--permutations','-p', type=int, help='list all permutations of the snippet')
parser.add_argument('--words','-w', type=int, help='list all dict words with combinations of chars of length x')

args = parser.parse_args()
snippet = args.snippet.lower()

def letter_map(word):
    map = {}
    for letter in word:
        if letter not in map: map[letter] = 0
        map[letter] += 1
    return map

with open('/usr/share/dict/words') as f:
    words = f.readlines()

#matches = []
#for word in words:
#    if snippet in word.lower():
#        matches.append(word)

# list comprehensions: replaces above 4 lines + strips \n from output.
# first item is modifying final list output
# second item is the for loop (for word in words)
# third item is an optional condition (if snippet in word.lower())
matches = [word.strip() for word in words if snippet in word.lower()]
#print(matches)

# Further reduce lines by including print too and skipping matches[] list assignment.
print ([word.strip() for word in words if snippet in word.lower()])

if args.words:
    matches = []
    snippet_map = letter_map(snippet.lower())
    print(f"Snippet: {snippet_map}")
    for word in words:
        pattern = re.compile('[\W_]+')
        word = pattern.sub('',word.strip().lower())
        word_map = letter_map(word)
        count = 0
        for letter in word:
            if letter in snippet_map.keys():
                if word_map.get(letter) <= snippet_map.get(letter):
                    count += 1
                    if len(word) == count and len(word) > args.words-1:
                        print(f"Word: {word_map}")
                        matches.append(word)
    print(set(sorted(matches)))

if args.permutations:
    perm_out = list(permutations(snippet, args.permutations))
    perm_count = len(perm_out)
    print(f"Found {perm_count} permutations (length={args.permutations}) of {snippet}. \nOUTPUT:\n{perm_out}")
