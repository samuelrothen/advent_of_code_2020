# Advent of Code Day 12


import numpy as np


def calcManhDistPart1(actions):
    x = 0
    y = 0
    ori = 0
    for act, val in actions:
        if act == 'N':
            y += val
        elif act == 'S':
            y -= val
        elif act == 'E':
            x += val
        elif act == 'W':
            x -= val
        elif act == 'L':
            ori += val
        elif act == 'R':
            ori -= val
        elif act == 'F':
            x += int(round(np.cos(np.radians(ori)),0)) * val
            y += int(round(np.sin(np.radians(ori)),0)) * val
    return abs(x) + abs(y)


def rotatePoint(x, y, deg):
    x_rot = np.cos(np.radians(-deg)) * x + np.sin(np.radians(-deg)) * y
    y_rot = np.sin(np.radians(deg)) * x + np.cos(np.radians(deg)) * y
    return (int(round(x_rot, 0)), int(round(y_rot, 0)))


def calcManhDistPart2(actions):
    wx = 10
    wy = 1
    sx = 0
    sy = 0
    for act, val in actions:
        if act == 'N':
            wy += val
        elif act == 'S':
            wy -= val
        elif act == 'E':
            wx += val
        elif act == 'W':
            wx -= val
        elif act == 'L':
            wx, wy = rotatePoint(wx, wy, val)
        elif act == 'R':
            wx, wy = rotatePoint(wx, wy, -val)
        elif act == 'F':
            sx += wx * val
            sy += wy * val
    return abs(sx) + abs(sy)


with open ('input/day12.txt', 'r') as f:
    actions = [(line[0], int(line[1:])) for line in f.read().split()]


print(f'Part 1: {calcManhDistPart1(actions)}')
print(f'Part 1: {calcManhDistPart2(actions)}')




