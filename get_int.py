#!/usr/bin/python
# -*- encoding=utf-8 -*-


def get_int(start_message, error_message, end_message):
    print(start_message)
    while True:
        try:
            i = int(input())
            print(end_message)
            return i
        except:
            print(error_message)

if __name__ == '__main__':
    x = get_int('input int:', 'wrong', 'ok')
    print(x)
