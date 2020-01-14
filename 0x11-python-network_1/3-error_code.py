#!/usr/bin/python3
"""
This module contains a program that print
the error messages of the http request
"""
import urllib.request
import sys
import urllib.error

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as f:
            html = f.read().decode()
            print(html)
    except urllib.error.HTTPError as error:
        error = error.code
        print("Error code: {}".format(error))
