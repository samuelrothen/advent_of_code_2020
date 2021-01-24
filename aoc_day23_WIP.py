# Advent of Code Day 23


def pick_up(cups):
    pick = cups[1:4]
    cups = [cups[0]] + cups[4:]
    return pick, cups


def find_dest(cups, pick, max_cup):
    dest = cups[0] - 1
    while dest in pick or dest not in cups:
        dest -= 1
        if dest <= 0:
            dest = max_cup
    ix_dest = cups.index(dest)
    return ix_dest

def place_cups(cups, ix_dest, pick):
    cups = cups[:ix_dest] + [cups[ix_dest]] + pick + cups[ix_dest + 1:]
    cups = cups[1:] + [cups[0]]
    return cups

def play_game(cups, n_moves):
    max_cup = max(cups)
    for move in range(n_moves):
        pick, cups = pick_up(cups)
        ix_dest = find_dest(cups, pick, max_cup)
        cups = place_cups(cups, ix_dest, pick)
    return cups


def solve_part1(cups):
    cups = play_game(cups, 10)
    ix_1 = cups.index(1)
    solution = cups[ix_1 + 1:] + cups[:ix_1]
    solution = ''.join(map(str, solution))
    return solution

data = 398254716
cups = [int(x) for x in str(data)]


print(f'Part 1: {solve_part1(cups)}')








print(f'Part 2: {0}')
