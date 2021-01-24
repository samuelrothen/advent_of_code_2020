# Advent of Code Day 18 - Part 2


def find_sub_par(ex):
    sub_par = ''
    level = 0
    start = False
    for c in ex:
        if c != '(' and not start:
            continue
        elif c == '(':
            level += 1
            start = True
        elif c == ')':
            level -= 1
        if start:
            sub_par += c
        if level == 0 and start:
            return sub_par[1:-1]


def solve(ex):
    if '(' in ex:
        sub = find_sub_par(ex)
        num = str(solve(sub))
        ex = ex.replace("("+sub+")", num)
        return solve(ex)
    else:
        total = 1
        for add in ex.split("*"):
            total *= eval(add)
        return total


def calc_sum(data):
    results = []
    for ex in data:
        results.append(int(solve(ex)))
    return sum(results)


with open('../input/day18.txt', 'r') as f:
    data =  f.read().split('\n')


print(f'Part 2: {calc_sum(data)}')
