#!/usr/bin/python3
"""
sends a request to the URL and displays the body of the response
"""
import sys
import requests


if __name__ == "__main__":
    req = requests.get(sys.argv[1]
    if requests.get(sys.argv[1].status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(requests.get(sys.argv[1].text)
