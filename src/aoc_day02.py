# Advent of Code Day 2

import pandas as pd
import re


def check_pw_part1(text):
    pattern = '(\d+)-(\d+) ([a-z]): ([a-z]+)'
    c_min, c_max, c_search, password = re.findall(pattern, text)[0]
    c_min, c_max = int(c_min), int(c_max)
    c_count = password.count(c_search)
    if c_count >= c_min and c_count <= c_max:
        return True
    else:
        return False


def check_pw_part2(text):
    pattern = '(\d+)-(\d+) ([a-z]): ([a-z]+)'
    ix_1, ix_2, c_search, password = re.findall(pattern, text)[0]
    c_1 = password[int(ix_1)-1]
    c_2 = password[int(ix_2)-1]
    if (c_1 == c_search) ^ (c_2 == c_search):    
        return True
    else:
        return False


df = pd.read_csv('../input/day02.txt', names=['String'])
df['PW_Check_1'] = df['String'].apply(lambda text: check_pw_part1(text))
df['PW_Check_2'] = df['String'].apply(lambda text: check_pw_part2(text))


print(f'Part 1: {df["PW_Check_1"].value_counts().loc[True]}')
print(f'Part 2: {df["PW_Check_2"].value_counts().loc[True]}')
