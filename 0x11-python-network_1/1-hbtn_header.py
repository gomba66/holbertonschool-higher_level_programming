#!/usr/bin/python3
"""
This module contains a program that obtain
the header information of the http request
"""
import urllib.request
import sys

if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers['X-Request-Id'])
