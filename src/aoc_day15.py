# Advent of Code Day 15


def memory_game(starting_numbers, check_turn):
    turn = 1
    spoken = {}
    for start_num in starting_numbers:
        spoken[start_num] = turn
        turn += 1
    curr_num = 0
    
    while True:
        if turn >= check_turn:
            return curr_num
        elif curr_num in spoken:
            next_num = turn - spoken[curr_num]
        else:
            next_num = 0
        spoken[curr_num] = turn
        curr_num = next_num
        turn +=1


with open ('../input/day15.txt', 'r') as f:
    starting_numbers =  [int(n) for n in f.read().split(',')]


print(f'Part 1: {memory_game(starting_numbers, 2020)}')
print(f'Part 2: {memory_game(starting_numbers, 30000000)}')
