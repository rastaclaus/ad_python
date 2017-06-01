#!/usr/bin/env python
# -*- coding: utf-8 -*-
N_STRINGS = [
    ' --      --  --      --  --  --  --  -- ',
    '|  |   |   |   ||  ||   |      ||  ||  |',
    '|  |   |   |   ||  ||   |      ||  ||  |',
    '         --  --  --  --  --      --  -- ',
    '|  |   ||      |   |   ||  |   ||  |   |',
    '|  |   ||      |   |   ||  |   ||  |   |',
    ' --      --  --      --  --      --  -- ']

NUMS = {k: list() for k in range(10)}


def chunks(l, n):
    for i in range(0, len(l), n):
        yield(l[i:i+n])

for line in N_STRINGS:
    for i, chunk in enumerate(chunks(line, 4)):
        NUMS[i].append(chunk)


def print_numbers(nlist):
    print('x' + len(nlist)*4*'-' + 'x')
    for j in range(7):
        line = '|' + ''.join([NUMS[i][j] for i in nlist]) + '|'
        print(line)
    print('x' + len(nlist)*4*'-' + 'x')

if __name__ == '__main__':
    nums = list(map(int, list(input())))
    print_numbers(nums)
