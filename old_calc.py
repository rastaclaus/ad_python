#!/usr/bin/env python
# -*- coding: utf-8 -*-
N_SRUCT = [
           ' - ',
           '| |',
           ' - ',
           '| |',
           ' - ']
NUMS = {
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


def lcd_line(num, size, line_num):
    if line_num == 0:



def lcd_num(num, size):
    res = []
    for l in range(2 * size + 3):
        res.append(lcd_line(num, size, l))
    return res

