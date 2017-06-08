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
    d = next(dirs)
    filled = []
    for i in range(n**2):
        if (row, col) in filled \
                or row < 0 or row >= n \
                or col < 0 or col >= n:
            print(row, col)
            row -= d[0]
            col -= d[1]
            d = next(dirs)
            row += d[0]
            col += d[1]
        else:
            yield(i, row, col)
            filled.append((row, col))
            print(filled)
            row += d[0]
            col += d[1]


def get_sqmattr(n):
    return [[None for _ in range(n)] for _ in range(n)]


if __name__ == '__main__':
    from pprint import pprint
    n = int(input())
    matr = get_sqmattr(n)
    im = spirale_index(n)
    for i, row, col in im:
        matr[row][col] = i
    pprint(matr)
