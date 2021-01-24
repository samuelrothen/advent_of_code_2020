# Advent of Code Day 19


def parse_rules(data):
    rules = {}
    for line in data:
        key, r = line.split(': ')
        r = r.split('|')
        if r[0][0] == '"':
            r = r[0][1]
        else:
            r = [[int(x) for x in x.split()] for x in r]
        rules[int(key)] = r
    return rules


def check_msg(rules, msg, rule):
    if len(msg) < len(rule):
        return False
    if len(msg) == 0 or len(rule) == 0:
        return len(msg) == 0 and len(rule) == 0
    
    current_rule = rule.pop(0)
    if current_rule == 'a' or current_rule == 'b':
        if current_rule == msg[0]:
            return check_msg(rules, msg[1:], rule.copy())
    else:
        for sub_rule in rules[current_rule]:
            if check_msg(rules, msg, list(sub_rule) + rule.copy()):
                return True
    return False


def sum_valid_msgs(messages, rules):
    n_valid = 0
    for msg in messages:
        rule_0 = rules[0][0].copy()
        if check_msg(rules, msg, rule_0):
            n_valid += 1
    return n_valid


with open('../input/day19.txt', 'r') as f:
    data_rules, data_messages =  f.read().split('\n\n')
    data_rules = data_rules.split('\n')
    data_messages = data_messages.split('\n')


rules = parse_rules(data_rules)


print(f'Part 1: {sum_valid_msgs(data_messages, rules)}')


rules[8] = [[42], [42, 8]]
rules[11] = [[42, 31], [42, 11, 31]]

print(f'Part 2: {sum_valid_msgs(data_messages, rules)}')




