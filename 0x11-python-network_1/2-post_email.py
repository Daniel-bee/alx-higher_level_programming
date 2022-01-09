#!/usr/bin/python3
"""
sends a request to the URL and displays the body of the response
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":

    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
