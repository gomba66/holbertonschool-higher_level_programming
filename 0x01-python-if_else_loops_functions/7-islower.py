#!/usr/bin/python3
def islower(c):
    if (ord(c) - 32) >= 65 and (ord(c) - 32) <= 90:
        return True
    else:
        return False
