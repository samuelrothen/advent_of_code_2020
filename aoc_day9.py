# Advent of Code Day 9


def check_sum(numbers, n_find):
    for i, n1 in enumerate(numbers):
        for j, n2 in enumerate(numbers[i+1:]):
            n_sum = n1 + n2
            if n_sum == n_find:
                return True
    return False


def find_num(data, n_pre):
    for ix in range(n_pre, len(data)):
        if not check_sum(data[0:ix], data[ix]):
            return data[ix]


with open ('input/day9.txt', 'r') as f:
    data = [int(line) for line in f.read().splitlines()]


inval_num = find_num(data, 25)







print(f'Part 1: {find_num(data, 25)}')
print(f'Part 2: {0}')