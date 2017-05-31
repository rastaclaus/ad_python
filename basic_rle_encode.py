#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

if __name__ == '__main__':
    instr = 'a2a11b5c2CaB'
    # instr = input()
    nums = re.compile('(\d+)([A-Za-z]){1}')
    inlist = list(instr)
    coded = nums.finditer(instr)
    bias = 0
    for res in coded:
        len0 = len(inlist)
        start = res.start() + bias
        end = res.end() + bias
        inlist[start:end] = int(res.groups()[0]) * res.groups()[1]
        bias += len(inlist) - len0
    print(''.join(inlist))
