#!/usr/bin/env python
# -*- coding: utf-8 -*-

ALPHABET = list(' abcdefghijklmnopqrstuvwxyz')
HALPHABET = list(map(chr, range(0x1f600, 0x1f650)))


def get_sym(n, syms=ALPHABET):
    return syms[n % len(syms)]


def get_num(c, syms=ALPHABET):
    return syms.index(c)


if __name__ == '__main__':
    step = int(input())
    line = input().strip()
    res = ""
    for c in line:
        res += get_sym(get_num(c, HALPHABET) + step, HALPHABET)
    print('Result: "{}"'.format(res))
