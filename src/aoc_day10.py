# Advent of Code Day 10


import numpy as np


def get_diff(data):
    data = np.sort(data)
    data = np.insert(data, 0, 0)
    data = np.insert(data, data.size, np.max(data) + 3)
    diff = np.diff(data)
    return np.count_nonzero(diff == 1) * np.count_nonzero(diff == 3)


def get_arrangements(data):
    data = np.sort(data)
    arrang={0:1}
    for adapt in data:
        arrang[adapt] = 0
        if adapt - 1 in arrang:
            arrang[adapt] += arrang[adapt - 1]
        if adapt - 2 in arrang:
            arrang[adapt] += arrang[adapt - 2]
        if adapt - 3 in arrang:
            arrang[adapt] += arrang[adapt - 3]
    return arrang[max(arrang)]


data = np.loadtxt('../input/day10.txt',dtype=int)


print(f'Part 1: {get_diff(data)}')
print(f'Part 2: {get_arrangements(data)}')
