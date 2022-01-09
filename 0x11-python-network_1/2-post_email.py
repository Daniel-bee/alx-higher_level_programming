#!/usr/bin/python3
"""

"""
import urllib.request
from sys import argv

if __name__ == "__main__":
    val = {'email': argv[2]}
    data = urllib.parse.urlencode(val)
    data = data.encode('ascii')
    req = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(req) as response:
        page = response.read()
        print(page.decode('utf-8'))
