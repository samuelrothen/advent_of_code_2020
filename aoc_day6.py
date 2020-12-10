# Advent of Code Day 6


def count_anyones_yes(answers_all):
    n_yes = 0
    for answers_group in answers_all:
        answers_group = answers_group.replace('\n', '')
        n_yes += len(set(answers_group))
    return n_yes


def count_everyones_yes(answers_all):
    n_yes = 0
    for answers_group in answers_all:
        answ_sets = [set(answ_person) for answ_person in answers_group.split('\n')]
        answ_unique = None
        for answ in answ_sets:
            if answ_unique == None:
                answ_unique = answ
            answ_unique = answ_unique.intersection(answ)
        n_yes += len(answ_unique)
    return n_yes



with open ('input/day6.txt', 'r') as f:
    answers_all = f.read().split('\n\n')


print(f'Part 1: {count_anyones_yes(answers_all)}')
print(f'Part 2: {count_everyones_yes(answers_all)}')