#!/usr/bin/env python
# -*- encoding=utf-8 -*-


if __name__ == '__main__':
    cache = {}
    n = int(input())
    for i in range(n):
        num = int(input())
        if num not in cache.keys():
            cache[num] = f(num)
        print(cache[num])
