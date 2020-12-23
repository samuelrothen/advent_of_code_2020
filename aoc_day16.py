# Advent of Code Day 16


import re
import numpy as np


def parse_data(data):
    rules = {}
    your_ticket = 0
    nearby_tickets = []
    yt = False
    nt = False
    pattern = '([\D\s]+): (\d+)-(\d+) or (\d+)-(\d+)'
    for line in data:
        if line == '':
            continue
        elif re.match(pattern, line):
            rule, a, b, c, d = re.findall(pattern, line)[0]
            rules[rule] = (int(a), int(b), int(c), int(d))
        elif line.startswith('your ticket'):
            yt = True
            nt = False
        elif line.startswith('nearby tickets'):
            nt = True
            yt = False
        elif yt:
            your_ticket = [int(n) for n in line.split(',')]
        elif nt:
            nearby_tickets.append([int(n) for n in line.split(',')])
    return rules, your_ticket, nearby_tickets


def calc_error(rules, your_ticket, nearby_tickets):  
    error = []
    ix_invalid = set()
    for i, ticket in enumerate(nearby_tickets):
        for num in ticket:
            valid = False
            for a, b, c, d in rules.values():
                if a <= num <= b or c <= num <= d:
                    valid = True
            if not valid:
                error.append(num)
                ix_invalid.add(i)
    for ix in sorted(ix_invalid, reverse = True):  
        del nearby_tickets[ix]
    return error, nearby_tickets


def get_ticket_cols(nearby_tickets):
    nearby_tickets = np.array(nearby_tickets)
    ticket_cols_dups = {}
    for col in range(nearby_tickets.shape[1]):
        ticket_cols_dups[col] = []
        for rule in rules:
            a, b, c, d = rules[rule]
            valid = True
            for row in range(nearby_tickets.shape[0]):
                num = nearby_tickets[row, col]
                if not (a <= num <= b or c <= num <= d):
                    valid = False
                    break
            if valid:
                ticket_cols_dups[col].append(rule)

    ticket_cols = {}
    while len(ticket_cols) < len(ticket_cols_dups):
        for col_dup, rules_dup in ticket_cols_dups.items():
            if len(rules_dup) == 1:
                ticket_cols[col_dup] = rules_dup[0]
        for rule in ticket_cols.values():
            for col_dup, rules_dup in ticket_cols_dups.items():
                if rule in rules_dup:
                    ticket_cols_dups[col_dup].remove(rule)
    return ticket_cols 


def get_result(ticket_cols, your_ticket):
    result = 1
    for col, field in ticket_cols.items():
        if field.startswith('departure'):
            result *= your_ticket[col]
    return result



with open ('input/day16.txt', 'r') as f:
    data =  f.read().split('\n')


rules, your_ticket, nearby_tickets_all = parse_data(data)
error, nearby_tickets = calc_error(rules, your_ticket, nearby_tickets_all)
ticket_cols = get_ticket_cols(nearby_tickets)

    
print(f'Part 1: {sum(error)}')
print(f'Part 2: {get_result(ticket_cols, your_ticket)}')
