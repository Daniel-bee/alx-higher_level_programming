#!/usr/bin/python3
"""script that fetches https://intranet.hbtn.io/status"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
        page = response.read()
        print("Body response:")
        print(f"    - type: {type(page)}")
        print(f"    - content: {page}")
        print(f"    - utf8 content: {page.decode('utf8')}")
