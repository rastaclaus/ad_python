#!/usr/bin/python


def insite(x):
    if x == -10 or \
        x > -5 and x <= 3 or \
        x > 8 and x < 12 or \
        x >= 16:
            return True
    return False


import sys

a = int(input())
print(insite(a))
