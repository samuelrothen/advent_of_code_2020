# Advent of Code Day 18 - Part 2


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


def rep_add(p, ex):
    par_add = re.findall('(\d+ [\+ \d+]+ \d+)', p)
    for p_add in par_add:
        ex = ex.replace(p_add, return_result(p_add), 1)
    return ex


def calc_expression(ex):
    par_pattern = '(\([\d+\s\+\*]+\))'
    while re.findall(par_pattern, ex):
        par = re.findall(par_pattern, ex)
        for p in par:
            ex = rep_add(p, ex)
            ex = ex.replace(p, return_result(p), 1)
    ex = rep_add(ex, ex)
    return return_result(ex)


def calc_sum(data):
    results = []
    for ex in data:
        results.append(int(calc_expression(ex)))
    return sum(results)


with open('input/day18.txt', 'r') as f:
    data =  f.read().split('\n')



print(f'Part 2: {calc_sum(data)}')

def calc_sum2(data):
    results = []
    for ex in data:
        results.append(int(calc_expression(ex)))
    return (results)


r=calc_sum2(data)


#%%



# ex='2 * 3 + (4 * 5)'

# # calc_expression(ex)

# par_pattern = '(\([\d+\s\+\*]+\))'
# while re.findall(par_pattern, ex):
#     par = re.findall(par_pattern, ex)
#     for p in par:
#         ex = rep_add(p, ex)
#         ex = ex.replace(p, return_result(p), 1)



# rep_add(ex, ex)


# # while re.findall(par_pattern, ex):
# #     par = re.findall(par_pattern, ex)
# #     for p in par:
# #         par_add = re.findall('(\d+ [\+ \d+]+ \d+)', p)
# #         for p_add in par_add:
# #             ex = ex.replace(p_add, return_result(p_add), 1)
# #         ex = ex.replace(p, return_result(p), 1)