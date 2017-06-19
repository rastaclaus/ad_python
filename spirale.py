#!/usr/bin/env/python
# -*- coding: utf-8 -*-


def directions():
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while True:
        for d in dirs:
            yield(d)


def fill_matrix(n):
    matr = get_sqmattr(n)
    row, col = 0, 0
    dirs = directions()
    nr, nc = next(dirs)
    for i in range(0, n**2):
        matr[row][col] = i+1
        if row + nr < 0 or row + nr >= n or col + nc < 0 or col + nc >= n \
                or matr[row + nr][col + nc]:
            nr, nc = next(dirs)
        row += nr
        col += nc
    return matr


def get_sqmattr(n):
    return [[None for _ in range(n)] for _ in range(n)]


def print_matr(matr):
    for row in matr:
        for col in row:
            print(col, end=' ')
        print()


if __name__ == '__main__':
    n = int(input())
    matr = fill_matrix(n)
    print_matr(matr)
