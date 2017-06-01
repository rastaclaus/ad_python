#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
RE_CODED = re.compile('(\d*)([A-Za-z]){1}')


def count_from_string(s):
    if s:
        return int(s)
    else:
        return 1


def split_decode_series(instr):
    coded = ((count_from_string(m.groups()[0]), m.groups()[1])
             for m in RE_CODED.finditer(instr))
    return coded


def decode_series(sds):
    return ''.join([s[0]*s[1] for s in sds])


def rle_decode(instr):
    return decode_series(split_decode_series(instr))

if __name__ == '__main__':
    instr = input()
    print(rle_decode(instr))
