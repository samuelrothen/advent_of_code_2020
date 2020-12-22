# Advent of Code Day 13


import numpy as np


def earliest_bus(t_start, busses):
    t_earliest = []
    for bus in busses:
        t_earliest.append(int(np.ceil(t_start / bus)) * bus)
    ix_earliest = np.argmin(t_earliest)
    t_wait = t_earliest[ix_earliest] - t_start
    return busses[ix_earliest] * t_wait


def earliest_timestamp(busses):
    t_start = 0
    stepsize = 1
    for bus, t_off in busses_p2:
        while t_start % bus != (bus - t_off) % bus:
            t_start += stepsize
        stepsize *= bus
    return t_start


with open ('input/day13.txt', 'r') as f:
    data =  f.read().split()
    t_start = int(data[0])
    busses_p1 = [int(bus) for bus in data[1].split(',') if bus != 'x']
    busses_p2 = [(int(bus), ix) for ix, bus in enumerate(data[1].split(',')) if bus != 'x' ]


print(f'Part 1: {earliest_bus(t_start, busses_p1)}')
print(f'Part 2: {earliest_timestamp(earliest_timestamp)}')

