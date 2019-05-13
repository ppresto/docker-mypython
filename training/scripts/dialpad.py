#!/usr/bin/env python3.7

import argparse
import itertools

parser = argparse.ArgumentParser(description="Find all the letter combinations of the numbers dialed")
parser.add_argument("number", help="Enter the phone number you want to dial")
args = parser.parse_args()

numberpad = {'0':[], '1':[], '2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z'], '#':[], '*':[] }

def getComboList(phonenumber):
    map = {}
    combos = []
    for num in phonenumber:
        if num not in map:
            map[num] = 0
        map[num] += 1
    for k,v in map.items():
        if numberpad[k]:
            combos.append(list(itertools.combinations_with_replacement(numberpad[k], v)))
    return combos

def printCombinations(lists):
    total = 0
    for combination in itertools.product(*lists):
        tmp = ''
        for i in combination:
            tmp = tmp + ''.join(i)
        print (f"{tmp}")
        total += 1
    print(f"{total} : Combinations Found")
    print(f"\nLists generated from {args.number}: ")
    for i in lists:
        print(i)



combos = getComboList(args.number)


printCombinations(combos)
