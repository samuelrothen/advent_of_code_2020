# Advent of Code Day 1

import numpy as np


def find_sum_two_n(numbers, n_find):
    for i, n1 in enumerate(numbers):
        for j, n2 in enumerate(numbers[i+1:]):
            n_sum = n1 + n2
            if n_sum == n_find:
                return n1 * n2
    return 0


def find_sum_three_n(numbers, n_find):
    for i,n1 in enumerate(numbers):
        rest = n_find - n1
        found = find_sum_two_n(numbers[i+1:], rest)
        if found:
            return found * n1


numbers = np.loadtxt('../input/day01.txt',dtype=int)
n_find = 2020

print(f'Part 1: {find_sum_two_n(numbers, n_find)}')
print(f'Part 2: {find_sum_three_n(numbers, n_find)}')

