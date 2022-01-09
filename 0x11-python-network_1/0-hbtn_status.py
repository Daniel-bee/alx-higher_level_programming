#!/usr/bin/python3
"""script that fetches https://intranet.hbtn.io/status"""
import urllib.request


with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
    page = response.read()
    print("Body response:")
    print(f"\t - type: {type(page)}")
    print(f"\t - content: {page}")
    print(f"\t - utf8 content: {page.decode('utf8')}")
