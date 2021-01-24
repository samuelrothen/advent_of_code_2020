# Advent of Code Day 22


def parse_data(data):
    cards = {}
    for i, p in enumerate(data):
        cards[f'P{i+1}'] = [int(x) for x in p.split('\n')[1:]]
    return cards


def play_game(cards):
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
    
    return win, cards


def calc_score(win,cards):
    score = 0
    for i, c in enumerate(cards[win]):
        score += c * (len(cards[win]) - i)
    return score


def play_rec_combat(cards):
    memory = []
    memory.append(tuple(cards['P1'] + [0] + cards['P2']))
    
    while len(cards['P1']) > 0 and len(cards['P2']) > 0:
        cP1 = cards['P1'].pop(0)
        cP2 = cards['P2'].pop(0)
        
        if cP1 <= len(cards['P1']) and cP2 <= len(cards['P2']):
                sub_deck = cards.copy()
                sub_deck['P1'] = sub_deck['P1'][:cP1]
                sub_deck['P2'] = sub_deck['P2'][:cP2]
                sub_win, sub_deck = play_rec_combat(sub_deck)
                if sub_win == 'P1':
                    cards['P1'] = cards['P1'] + [cP1, cP2]
                elif sub_win == 'P2':
                    cards['P2'] = cards['P2'] + [cP2, cP1]

        elif cP1 > cP2:
            cards['P1'] = cards['P1'] + [cP1, cP2]

        elif cP2 > cP1:
            cards['P2'] = cards['P2'] + [cP2, cP1]
        
        m = tuple(cards['P1'] + [0] + cards['P2'])
        if m in memory:
            return 'P1', cards
        else:
            memory.append(m)
    
    if len(cards['P1']) == 0:
        win = 'P2'
    else:
        win = 'P1'
    return win, cards


with open('input/day22.txt', 'r') as f:
    data =  f.read().split('\n\n')


cards = parse_data(data)
win_part1, winning_cards_part1 = play_game(cards)

print(f'Part 1: {calc_score(win_part1,winning_cards_part1)}')


cards = parse_data(data)
win_part2, winning_cards_part2 = play_rec_combat(cards)
print(f'Part 2: {calc_score(win_part2, winning_cards_part2)}')
