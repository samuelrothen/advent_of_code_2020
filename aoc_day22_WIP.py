# Advent of Code Day 22


with open('input/day22.txt', 'r') as f:
    data =  f.read().split('\n\n')


# data = '''Player 1:
# 9
# 2
# 6
# 3
# 1

# Player 2:
# 5
# 8
# 4
# 7
# 10'''.split('\n\n')


cards = {}
for i, p in enumerate(data):
    cards[f'P{i+1}'] = [int(x) for x in p.split('\n')[1:]]


while len(cards['P1']) > 0 and len(cards['P2']) > 0:
    cP1 = cards['P1'].pop(0)
    cP2 = cards['P2'].pop(0)
    if cP1 > cP2:
        cards['P1'] = cards['P1'] + [cP1, cP2]
    elif cP2 > cP1:
        cards['P2'] = cards['P2'] + [cP2, cP1]

if len(cards['P1']) == 0:
    win = 'P2'
else:
    win = 'P1'

score = 0
for i, c in enumerate(cards[win]):
    score += c * (len(cards[win]) - i)


print(f'Part 1: {score}')



