# Advent of Code Day 7


import re


def parse_colors(bag_rules):
    color_rules = {}
    for rule in bag_rules:
        bags = re.findall('(\w+ \w+) bag', rule)
        first_bag = bags[0]
        bag_contains = bags[1:]
        if bag_contains[0] != 'no other':
            color_rules[first_bag] = bag_contains
    return color_rules


def get_unique_colors(color_rules):
    unique_colors = set()
    for key in color_rules:
        unique_colors.add(key)
        for value in color_rules[key]:
            unique_colors.add(value)
    return unique_colors


def search_color(color_rules, color):
    pass



for key in color_rules:
    if 'shiny gold' in color_rules[key]:
        return True
    else:
        for color in color_rules[key]:
            color_rules[color]


with open ('input/day7.txt', 'r') as f:
    bag_rules = f.read().split('\n')

color_rules = parse_colors(bag_rules)
unique_colors = get_unique_colors(color_rules)



# print(f'Part 1: {1}')
# print(f'Part 2: {1}')