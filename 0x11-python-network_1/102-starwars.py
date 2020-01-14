#!/usr/bin/python3
"""
This module contains a program that sends
a POST request to the URL with an email address
"""
import urllib.parse
import urllib.request
from sys import argv

if __name__ == "__main__":

    email = {'email': argv[2]}
    data = urllib.parse.urlencode(email)
    data = data.encode('ascii')
    r = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(r) as f:
        print(str(f.read(), 'utf-8'))
