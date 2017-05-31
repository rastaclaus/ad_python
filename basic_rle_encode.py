#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

if __name__ == '__main__':
    # instr = input()
    nums = re.compile('\d+')
    instr = 'a2ab45c2CaB'
    for m in nums.finditer(instr):
        print(m.start(), m.group())
