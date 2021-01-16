# Advent of Code Day 18 - Part 1


def calc_expression(ex):
    par = []
    level = 0
    result = 0
    operator = '+'
    for c in ex:
        if c == ' ':
            continue
        if c == '(':
            level += 1
        elif c == ')':
            level -= 1
            if level == 0:
                c = str(calc_expression(par[1:]))
                par = []
        if level:
            par.append(c)
        else:
            if c in '+*':
                operator = c
            else:
                result = eval(str(result) + operator + c)
    return result
        

def calc_sum(data):
    results = []
    for ex in data:
        results.append(int(calc_expression(ex)))
    return sum(results)


with open('input/day18.txt', 'r') as f:
    data =  f.read().split('\n')


print(f'Part 1: {calc_sum(data)}')
