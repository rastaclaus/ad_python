#!/usr/bin/env python
# -*- encoding=utf-8 -*-

if __name__ == '__main__':
    instr = input()
    substr = input()
    res = list()
    for i in range(len(instr) - len(substr) + 1):
        if instr[i:i+len(substr)] == substr:
            res.append(str(i))
    if res:
        print(' '.join(res))
    else:
        print(-1)
