#!/usr/bin/env python
# -*- encoding=utf-8 -*-


def hanoy(q, fr, to, bf):
    if q == 0:
        return
    hanoy(q-1, fr, bf, to)
    print(fr, '-',  to)
    hanoy(q-1, bf, to, fr)

if __name__ == '__main__':
    q = int(input())
    hanoy(q, 1, 3, 2)
