# Advent of Code Day 4


import re


def byr(pp_dict):
    return 1900 <= int(pp_dict['byr']) <= 2002

def iyr(pp_dict):
    return 2010 <= int(pp_dict['iyr']) <= 2020

def eyr(pp_dict):
    return 2020 <= int(pp_dict['eyr']) <= 2030

def hgt(pp_dict):
    val = pp_dict['hgt']
    if val.endswith('cm'):
        return 150 <= int(val[:-2]) <= 193
    if val.endswith('in'):
        return 59 <= int(val[:-2]) <= 76
    return 0

def hcl(pp_dict):
    return re.match('#[0-9a-f]{6}', pp_dict['hcl'])

def ecl(pp_dict):
    return pp_dict['ecl'] in 'amb blu brn gry grn hzl oth'

def pid(pp_dict):
    return re.match('^\d{9}$', pp_dict['pid'])


def check_PP_part1(pp_dict, required):
    for key in required:
        if key not in pp_dict:
            return 0
    return 1


def check_PP_part2(pp_dict, required):
    for key in required:
        if key not in pp_dict:
            return 0
    if not byr(pp_dict):
        return 0
    if not iyr(pp_dict):
        return 0
    if not eyr(pp_dict):
        return 0
    if not hgt(pp_dict):
        return 0
    if not hcl(pp_dict):
        return 0
    if not ecl(pp_dict):
        return 0
    if not pid(pp_dict):
        return 0
    return 1



with open ('input/day04.txt', 'r') as f:
    passports_list = f.read().split('\n\n')

required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

pattern = '(\w{3}):(\S+)'
n_valid_part1=0
n_valid_part2=0
for i, pp_raw in enumerate(passports_list):
    pp_clean = pp_raw.replace('\n', ' ')
    pp_fields = re.findall(pattern, pp_clean)
    pp_dict = dict((key, val) for key, val in pp_fields)
    n_valid_part1 += check_PP_part1(pp_dict, required)
    n_valid_part2 += check_PP_part2(pp_dict, required)


print(f'Part 1: {n_valid_part1}')
print(f'Part 2: {n_valid_part2}')