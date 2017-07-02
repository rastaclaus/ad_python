# -*- conding: utf-8 -*-
"""
rome to digits module
"""
from collections import OrderedDict

ROME_DIGITS = {
    "I": 1,
    "IV": 4,
    "V": 5,
    "IX": 9,
    "X": 10,
    "XL": 40,
    "L": 50,
    "XC": 90,
    "C": 100,
    "CD": 400,
    "D": 500,
    "CM": 900,
    "M": 1000
}

if __name__ == '__main__':
    rs = input()
    rn = 0
    rds = OrderedDict(sorted(ROME_DIGITS.items(), key=lambda t: t[1])[::-1])
    for key in rds:
        while rs.startswith(key):
            rn += rds[key]
            rs = rs[len(key):]
    print(rn)
