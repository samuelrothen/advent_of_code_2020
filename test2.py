import re

def find_par(s):
    """returns first parenthese substring"""
    sub = ""
    par = 0
    start = False
    for c in s:
        if c != '(' and not start:
            continue
        elif c == '(':
            par += 1
            start = True
        elif c == ')':
            par -= 1
        if start:
            sub += c
        if par == 0 and start:
            return sub[1:-1]
        
assert find_par("1 + (1+1) + 1)") == "1+1"

            
def solve(s):
    if "(" in s:
        sub = find_par(s)
        num = str(solve(sub))
        s = s.replace("("+sub+")", num)
        return solve(s)
    else:
        # numbers and operators only
        total = 1
        for add in s.split("*"):
            # no-par additions
            total *= eval(add)
        return total



with open ('input/day18.txt', 'r') as f:
    data =  f.read().split('\n')


result = 0
for line in data:
    result += solve(line.strip())







