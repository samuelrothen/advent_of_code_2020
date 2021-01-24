# Advent of Code Day 14


import re
import itertools


def return_sum_mem_part1(data):
    mem  = {}
    mask = []
    for line in data:
        if 'mask' in line:
            mask = [(m.start(0), m.group()) for m in re.finditer('\d', line[7:])]
        elif 'mem' in line:
            mem_ix, mem_val_int = list(map(int, re.findall('mem\[(\d+)\] = (\d+)', line)[0]))
            mem_val_bin = bin(mem_val_int)[2:]
            mem_val_bin = list(mem_val_bin.zfill(36))
            
            for pos, val in mask:
                mem_val_bin[pos] = val
            mem_val_mask = ''.join(mem_val_bin)
            mem_val_mask = int(mem_val_mask, 2)
            mem[mem_ix] = mem_val_mask
    return sum(mem.values())


def return_sum_mem_part2(data):
    mem  = {}
    mask = []
    for line in data:
        if 'mask' in line:
            mask = [(m.start(0), m.group()) for m in re.finditer('[1X]', line[7:])]
            X_ix = [m.start(0) for m in re.finditer('X', line[7:])]
        elif 'mem' in line:
            mem_ix, mem_val_int = list(map(int, re.findall('mem\[(\d+)\] = (\d+)', line)[0]))
            mem_ix_bin = bin(mem_ix)[2:]
            mem_ix_bin = list(mem_ix_bin.zfill(36))
            
            for pos, val in mask:
                mem_ix_bin[pos] = val
            
            n_floating = len(X_ix)
            bin_combinations = list(itertools.product([0, 1], repeat=n_floating))
            
            for comb in bin_combinations:
                for i, bin_val in enumerate(comb):
                    mem_ix_bin[X_ix[i]] = str(bin_val)
                mem_ix_mask = ''.join(mem_ix_bin)
                mem_ix_mask = int(mem_ix_mask, 2)
                mem[mem_ix_mask] = mem_val_int
    return sum(mem.values())


with open ('../input/day14.txt', 'r') as f:
    data =  f.read().split('\n')


print(f'Part 1: {return_sum_mem_part1(data)}')
print(f'Part 2: {return_sum_mem_part2(data)}')
