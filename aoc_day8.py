# Advent of Code Day 8


def parse_file(file):
    with open (file, 'r') as f:
        data=[]
        for line in f.read().splitlines():
            op, num = line.split()
            num = int(num)
            data.append([op, num])
    return data


def execute_prog_part1(file):
    data = parse_file(file)
    acc = 0
    op_id = 0
    executed = set()
    while op_id not in executed:
        executed.add(op_id)
        op, num = data[op_id]
        if op == 'acc':
            acc += num
            op_id += 1
        elif op == 'jmp':
            op_id += num
        elif op == 'nop':
            op_id += 1
    return acc


def change_op(data, ix):
    if data[ix][0] == 'jmp':
        data[ix][0] = 'nop'
    elif data[ix][0] == 'nop':
        data[ix][0] = 'jmp'


def execute_prog_part2(file):
    data = parse_file(file)
    for ix_global in range(len(data)):
        data = parse_file(file)
        change_op(data, ix_global)
        acc = 0
        op_id = 0
        executed = set()
        while op_id not in executed:
            if op_id >= len(data):
                return acc
            executed.add(op_id)
            op, num = data[op_id]
            if op == 'acc':
                acc += num
                op_id += 1
            elif op == 'jmp':
                op_id += num
            elif op == 'nop':
                op_id += 1


print(f'Part 1: {execute_prog_part1("input/day8.txt")}')
print(f'Part 2: {execute_prog_part2("input/day8.txt")}')

