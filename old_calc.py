#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from pprint import pprint

NUM_STRUCT = {
        0: [0, 1, 2, 4, 5, 6],
        1: [2, 5],
        2: [0, 2, 3, 4, 6],
        3: [0, 2, 3, 5, 6],
        4: [1, 2, 3, 5],
        5: [0, 1, 3, 5, 6],
        6: [0, 1, 3, 4, 5, 6],
        7: [0, 2, 5],
        8: [0, 1, 2, 3, 4, 5, 6],
        9: [0, 1, 2, 3, 5, 6]
}


def segments_struct(size):
    return {
            0: ([0], range(1, 1+size)),
            1: (range(1, 1+size), [0]),
            2: (range(1, 1+size), [1+size]),
            3: ([1+size], range(1, 1+size)),
            4: (range(2+size, 2*size+2), [0]),
            5: (range(2+size, 2*size+2), [1+size]),
            6: ([2*size+2], range(1, 1+size))
    }


def segment_fill(segment):
    if segment % 3 == 0:
        return '-'
    else:
        return '|'


def is_filled(segment_struct, line, col):
    if line in segment_struct[0] and col in segment_struct[1]:
        return True
    else:
        return False


def lcd_num(num, size):
    width = size + 2
    heigth = 2 * size + 3

    segs_struct = segments_struct(size)
    num_struct = NUM_STRUCT[num]
    res = [list(' ' * width) for _ in range(heigth)]

    for line in range(heigth):
        for col in range(width):
            for segment in num_struct:
                if is_filled(segs_struct[segment], line, col):
                    res[line][col] = segment_fill(segment)

    return res

if __name__ == '__main__':
    for i in range(10):
        ln = lcd_num(i, 2)
        for l in ln:
            print(''.join(l), ';')
