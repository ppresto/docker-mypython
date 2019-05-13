#!/usr/bin/env python3.7

import json
import urllib.request
import re

def flatten_json(nested_json):
    """
        Flatten json object with nested keys into a single level.
        Args:
            nested_json: A nested json object.
        Returns:
            The flattened json object if successful, None otherwise.
    """
    out = {}

    def flatten(x, name=''):
        #if type(x) is dict:
        if isinstance(x, dict):
            for a in x:
                flatten(x[a], name + a + '_')
        #elif type(x) is list:
        elif isinstance(x, list):
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(nested_json)
    return out


def extract_values(obj, key):
    """Pull all values of specified key from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    results = extract(obj, arr, key)
    return results

#pattern = re.compile('[\W_]+')
#word = pattern.sub('',word.strip().lower())


# open the URL
url = "https://swapi.co/api/people/"
headers={'User-Agent': 'Mozilla/5.0'}
req = urllib.request.Request(url, headers = headers)
# data = json.load(urllib.request.urlopen(req))
data = urllib.request.urlopen(req).read().decode('utf-8')

jobject = json.loads(data)

print(f"Show Exact Values for 'name':\n {extract_values(jobject, 'name')}")
print(f"Show Exact Values for 'height':\n {extract_values(jobject, 'height')}")
print(f"\n Show Flattened JSON structure: \n {flatten_json(jobject)}")

exampleString = '''
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97 years old, and his grandfather, Oscar, is 102.
'''

ages = re.findall(r'\d{1,3}',exampleString)
names = re.findall(r'[A-Z][a-z]*',exampleString)
print(ages)
print(names)

stringList = exampleString.split()
print (stringList)
for word in stringList:
    if word[0].isupper():
        print(f"Name: {word}")
    if re.findall(r'\d{1,3}',word):
        print(f"Ages: {word}")

#jdump = json.dumps(data, indent=4, sort_keys=True)
#print(jdump)
#jdata = json.loads(jdump)
# print the result
#print(jdata)
