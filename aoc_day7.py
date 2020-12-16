# Advent of Code Day 7


import re


def parse_colors(bag_rules):
    color_rules = {}
    numbers_rules = {}
    for rule in bag_rules:
        bags = re.findall('(\w+ \w+) bag', rule)
        n_bags = [int(n) for n in re.findall("\d+", rule)]
        first_bag = bags[0]
        bag_contains = bags[1:]
        color_rules[first_bag] = bag_contains
        numbers_rules[first_bag] = n_bags
    return color_rules, numbers_rules


def search_color(color_rules, check_color):
    if check_color == 'no other':
        return False
    elif 'shiny gold' in color_rules[check_color]:
        return True
    else:
        for contained_color in color_rules[check_color]:
            if search_color(color_rules, contained_color):
                return True


def sum_bags(color_rules, numbers_rules, check_color, mulip = 1):
    colors = color_rules[check_color]
    n_bags = numbers_rules[check_color]
    n_bags_total = 0
    for color, n in zip(colors, n_bags):
        n_bags_total += n * sum_bags(color_rules, numbers_rules, color, mulip * n)
    return n_bags_total + 1


def check(bag_rules):
    n_found = 0
    color_rules, numbers_rules = parse_colors(bag_rules)
    for key in color_rules:
        if search_color(color_rules, key):
            n_found += 1
    return n_found



with open ('input/day7.txt', 'r') as f:
    bag_rules = f.read().split('\n')

color_rules, numbers_rules = parse_colors(bag_rules)

print(f'Part 1: {check(bag_rules)}')
print(f'Part 2: {sum_bags(color_rules, numbers_rules, "shiny gold", mulip = 1) - 1}')


