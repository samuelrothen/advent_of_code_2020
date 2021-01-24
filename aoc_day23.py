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


def solve_part1(cups, n_moves):
    cups = play_game(cups, n_moves)
    ix_1 = cups.index(1)
    solution = cups[ix_1 + 1:] + cups[:ix_1]
    solution = ''.join(map(str, solution))
    return solution


def solve_part2(cups):
    cups = cups + list(range(max(cups) + 1, 1000001))
    cups = play_game(cups, 10000000)
    ix_1 = cups.index(1)
    solution = cups[ix_1 + 1] * cups[ix_1 + 2]
    return solution


data = 398254716
cups = [int(x) for x in str(data)]


print(f'Part 1: {solve_part1(cups, 100)}')



class LinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None

linkedl = {}
prev_cup = None

cups = cups + list(range(max(cups) + 1, 1000001))
for cup in cups:
    curr = LinkedList(cup)
    linkedl[cup] = curr
    if prev_cup:
        prev_cup.next = curr
    prev_cup = curr
prev_cup.next = linkedl[cups[0]]

curr = None
for move in range(10000000):
    # Go to next position for every move
    if curr:
        curr = curr.next
    else:
        curr = linkedl[cups[0]]
    
    # Pick up the cups 
    pick = [curr.next, curr.next.next, curr.next.next.next]
    curr.next = pick[-1].next
    
    # Find the destination
    dest_val = curr.data - 1
    while dest_val in [v.data for v in pick]:
        dest_val -= 1
    if dest_val < 1:
        dest_val = 1000000
    dest = linkedl[dest_val]
    
    # Place the cups in new order
    pick[-1].next = dest.next
    dest.next = pick[0]


print(f'Part 2: {linkedl[1].next.data * linkedl[1].next.next.data}')
