#!/usr/bin/bash
# -*- coding: utf-8 -*-

from itertools import groupby

if __name__ == '__main__':
    instr = input()
    res = ""
    for k, g in groupby(instr):
        l = len(list(g))
        if l > 1:
            res += str(l)
        res += k
    print(res)
