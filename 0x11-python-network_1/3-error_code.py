#!/usr/bin/python3
"""
sends a request to the URL and displays the body of the response
"""
import urllib.request
from sys import argv

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as response:
            page = response.read()
            print(page.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
