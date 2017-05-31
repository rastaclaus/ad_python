#!/usr/bin/python
# pylint: disable=C0103
"""Life game"""
# import sys


class Field:
    "field of life game"

    def __init__(self, width, height, item):
        self.width = width
        self.height = height
        self.matrix = list(map(list, item.split('\n')))

    def __repr__(self):
        res = [''.join(row) for row in self.matrix]
        return '\n'.join(res)

    def get_index(self, x, y):
        "return row, col of point"
        return y % self.height, x % self.width

    def set_value(self, x, y, value):
        "set value of field"
        row, col = self.get_index(x, y)
        self.matrix[row][col] = value

    def get_value(self, x, y):
        "get value of field"
        row, col = self.get_index(x, y)
        return self.matrix[row][col]

    def get_neighbors(self, x, y):
        "get list of neighbors coords pair"
        res = [self.get_index(x + dx, y + dy)
               for dx in range(-1, 2) for dy in range(-1, 2)
               if not(dx == 0 and dy == 0)]
        return res

    def __next__(self):
        new_field = Field(self.width, self.height, self.__repr__())
        for x in range(self.width):
            for y in range(self.height):
                neighbors_values = [self.matrix[row][col]
                                    for row, col in self.get_neighbors(x, y)]
                life_count = neighbors_values.count('X')
                if life_count == 3:
                    new_field.set_value(x, y, 'X')
                elif life_count < 2 or life_count > 3:
                    new_field.set_value(x, y, '.')
        return new_field


import sys
h, w = map(int, next(sys.stdin).split())
lines = [next(sys.stdin).rstrip() for _ in range(h)]
f = Field(w, h, '\n'.join(lines))
print(next(f))
