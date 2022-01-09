#!/usr/bin/python3
"""
sends a request to the URL and displays the value of the X-Request-Id variable
"""
import sys
import urllib.request


if __name__ == "__main__":

    with urllib.request.urlopen(urllib.request.Request(sys.argv[1])) as response:
        print(dict(response.headers).get("X-Request-Id"))
