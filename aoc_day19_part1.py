# Advent of Code Day 19




data='''0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"'''.split('\n')


rules = {}
for line in data:
    n=line.split(':')
    key, r = line.split(': ')
    r = r.split('|')
    if r[0][0] == '"':
        r = r[0][1]
    else:
        r = [x.split() for x in r]
    rules[key] = r








print(f'Part 1: {0}')