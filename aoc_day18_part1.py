# Advent of Code Day 18 - Part 1


import re


def return_result(exp_string):
    operator = ''
    result = ''
    for char in re.findall('(\d+|[()+*])', exp_string):
        if char in '() ':
            continue
        else:
            if char in '+*':
                operator = char
            else:
                result = eval(str(result) + operator + char)
    return str(result)


def calc_expression(ex):
    par_pattern = '(\([\d+\s\+\*]+\))'
    while re.findall(par_pattern, ex):
        par = re.findall(par_pattern, ex)
        for p in par:
            ex = ex.replace(p, return_result(p), 1)
    return return_result(ex)


def calc_sum(data):
    results = []
    for ex in data:
        results.append(int(calc_expression(ex)))
    return sum(results)


with open('input/day18.txt', 'r') as f:
    data =  f.read().split('\n')


print(f'Part 1: {calc_sum(data)}')
