#!/usr/bin/python
# pylint: disable=C0103
import numpy as np


def input_size():
    h, w = map(int, input().split())
    return w, h


def input_field_data(width, height):
    lines = [list(input()) for _ in range(height)]
    return np.array(lines)


def prepare_field(field_array):
    res = np.empty((field_array.shape[0] + 2,
                    field_array.shape[1] + 2), dtype=str)
    res.fill('.')
    res[1:-1, 1:-1] = field_array
    return res


def get_mines_count(fld, index):
    y, x = index
    return str(list(fld[y-1:y+2, x-1:x+2].flat).count('*'))


def print_field(fld):
    for row in fld:
        print(''.join(row))


if __name__ == '__main__':
    wdim, hdim = input_size()
    field = input_field_data(wdim, hdim)
    emptys = np.argwhere(field == '.') + 1
    pfield = prepare_field(field)
    for empty in emptys:
        cy, cx = empty
        pfield[cy, cx] = get_mines_count(pfield, empty)
    print_field(pfield[1:-1, 1:-1])
