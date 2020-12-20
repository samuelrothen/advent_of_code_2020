# Advent of Code Day 10 - Part 2


import copy


def return_occu_seats(seats, x, y):
    seat_check_array = [(-1, -1), (-1, 0), (-1, 1),
                        (0, -1),           (0, 1),
                        (1, -1),  (1, 0),  (1, 1)]
    counter = 0
    for check_y, check_x in seat_check_array:
        ny, nx = y, x
        while True:
            ny = ny + check_y
            nx = nx + check_x
            if nx < 0 or ny < 0:
                break
            if nx >= len(seats[0]) or ny >= len(seats):
                break
            if seats[ny][nx] == '#':
                counter += 1
                break
            elif seats[ny][nx] == 'L':
                break
    return counter


def calc_seats_new(seats):
    seats_new = copy.deepcopy(seats)
    for y, row in enumerate(seats):
        for x, seat in enumerate(row):
            n_occu = return_occu_seats(seats, x, y)
            if seat == '#' and n_occu >= 5:
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


print(f'Part 2: {solve(seats)}')



