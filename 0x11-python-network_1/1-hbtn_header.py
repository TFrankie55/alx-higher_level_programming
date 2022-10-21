#!/usr/bin/python3
"""displays the value of the X-Request-Id variable

Usage: ./1-hbtn_header.py <URL>'
"""
import sys
import urllib.request


if _name__  == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(deict(response.headers).get("X-Request-Id"))
