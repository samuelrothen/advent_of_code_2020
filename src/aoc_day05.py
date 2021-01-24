# Advent of Code Day 5


# Part 1
def search_position(input_string, stepsize, upper_half):
    position = 0
    for char in input_string:
        if char == upper_half:
            position += stepsize
        stepsize = stepsize // 2
    return position


def calc_seatID(input_string):
    row = search_position(input_string[:7], 64, 'B')
    col = search_position(input_string[7:], 4, 'R')
    seatID = row * 8 + col
    return seatID


with open ('../input/day05.txt', 'r') as f:
    seating_list = f.read().splitlines()

seatIDs = []
for seat_binary in seating_list:
    seatIDs.append(calc_seatID(seat_binary))


# Testing
assert calc_seatID('BFFFBBFRRR') == 567
assert calc_seatID('FFFBBBFRRR') == 119
assert calc_seatID('BBFFBBFRLL') == 820


# Part 2
for ID in range(max(seatIDs)):
    if ID not in seatIDs and ID-1 in seatIDs and ID+1 in seatIDs:
        my_seatID = ID
        break
    

print(f'Part 1: {max(seatIDs)}')
print(f'Part 2: {my_seatID}')
