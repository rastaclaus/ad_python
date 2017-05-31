#!/usr/bin/python
"""task3.7"""
# pylint: disable=C0103


def get_indexes(lst, number):
    """
    return list of indexes
    searched number in lst, or None if number not in lst
    """
    res = [ind for ind, num in enumerate(lst) if num == number]
    if res:
        return ' '.join(map(str, res))

if __name__ == '__main__':
    in_lst = list(map(int, input().split()))
    fnum = int(input())
    print(get_indexes(in_lst, fnum))
