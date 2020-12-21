# Advent of Code Day 11 - Part 1


import copy


def return_occu_seats(seats, x, y):
    seat_check_array = [(-1, -1), (-1, 0), (-1, 1),
                        (0, -1),           (0, 1),
                        (1, -1),  (1, 0),  (1, 1)]
    counter = 0
    for check_y, check_x in seat_check_array:
        check_x = check_x + x
        check_y = check_y + y
        if check_x < 0 or check_y < 0:
            continue
        if check_x >= len(seats[0]) or check_y >= len(seats):
            continue
        if seats[check_y][check_x] == '#':
            counter += 1
    return counter


def calc_seats_new(seats):
    seats_new = copy.deepcopy(seats)
    for y, row in enumerate(seats):
        for x, seat in enumerate(row):
            n_occu = return_occu_seats(seats, x, y)
            if seat == '#' and n_occu >= 4:
                seats_new[y][x] = 'L'
            elif seat == 'L' and n_occu == 0:
                seats_new[y][x] = '#'
    return seats_new


def solve(seats):
    while True:
        seats_new = calc_seats_new(seats)
        if seats == seats_new:
            break
        seats = seats_new
    flatten = [val for sublist in seats for val in sublist]
    return flatten.count('#')



with open ('input/day11.txt', 'r') as f:
    seats = [list(line) for line in f.read().split()]


print(f'Part 1: {solve(seats)}')



