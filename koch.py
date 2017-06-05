#!/usr/bin/env python
# -*- coding: utf-8 -*-


def koch_it(n, turn_list):
    for i in range(0, 4*len(turn_list)+3, 4):
        turn_list[i: i] = [60, -120, 60]

    if n == 1:
        return
    else:
        koch_it(n-1, turn_list)


def print_turns(turn_list):
    for turn in turn_list:
        print("turn", turn)


def turtle_koch_curve(turns, line_length=10):
    import turtle
    turtle.pu()
    turtle.setx(-900)
    turtle.sety(-200)
    turtle.pd()
    for turn in turns:
        turtle.forward(line_length)
        turtle.left(turn)
    turtle.forward(line_length)
    turtle.mainloop()


if __name__ == '__main__':
    n = int(input())
    turn_list = []
    koch_it(n, turn_list)
    turtle_koch_curve(turn_list, 5)
