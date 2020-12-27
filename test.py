import re

def calc(tokens):
    par = []
    parlevel = 0
    result = 0
    op = "+"
    for t in tokens:
        if t == "(":
            parlevel += 1
        elif t == ")":
            parlevel -= 1
            if parlevel == 0:
                t = str(calc(par[1:]))
                par = []
        if parlevel:
            par.append(t)
        else:
           if t in "+*":
               op = t
           else:
               result = eval(str(result) + op + t)
    return result

def solve(s):
    tokens = re.findall("\d+|[()+*]", s)
    return calc(tokens)

with open('input/day18.txt', 'r') as f:
    data =  f.read().split('\n')


result = 0
for line in data:
    result += solve(line.strip())






