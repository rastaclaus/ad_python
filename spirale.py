#!/usr/bin/env/python
# -*- coding: utf-8 -*-


def directions():
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while True:
        for d in dirs:
            yield(d)


def spirale_index(n):
    dirs = directions()
    row, col = 0, 0
    dir = next(dirs)
    count = 0
    l = n-1
    for i in range(n**2):
        yield (i, row, col)
        row, col = row + dir[0], col + dir[1]
        count += 1
        if count == l:
            count = 0
            dir = next(dirs)
            if dir == (-1, 0):
                l -= 1


def get_sqmattr(n):
    return [[None for _ in range(n)] for _ in range(n)]


if __name__ == '__main__':
    from pprint import pprint
    n = int(input())
    matr = get_sqmattr(n)
    im = spirale_index(n)
    pprint(matr)
    for i, row, col in im:
        print(i, row, col)
        matr[row][col] = i
        pprint(matr)
    pprint(matr)
