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


def find_sum(data, inval_num):
    ix1 = 0
    for ix1 in range(len(data)):
        for ix2 in range(ix1+1, len(data)):
            sum_num = sum(data[ix1:ix2])
            if sum_num > inval_num:
                break
            elif sum_num == inval_num:
                return min(data[ix1:ix2]) + max(data[ix1:ix2])
  

      
with open ('../input/day09.txt', 'r') as f:
    data = [int(line) for line in f.read().splitlines()]

inval_num = find_num(data, 25)

print(f'Part 1: {inval_num}')
print(f'Part 2: {find_sum(data, inval_num)}')