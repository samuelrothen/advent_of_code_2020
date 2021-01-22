# Advent of Code Day 21


import numpy as np
import pandas as pd


def parse_data(data):
    food_list = []
    for line in data:
        ingr, allerg = line.split(' (contains ')
        ingr = ingr.split()
        allerg = allerg[:-1].split(', ')
        food_list.append((ingr, allerg))
    return food_list


def return_unique(food_list):
    ingr, allerg = [], []
    for i, a in food_list:
        ingr += i
        allerg += a
    return set(ingr), set(allerg)


def return_allerg_df(food_list):
    ing_unique, alg_unique = return_unique(food_list)
    df = pd.DataFrame(np.ones((len(ing_unique), len(alg_unique))), columns = alg_unique, index = ing_unique)
    
    for i_entry, a_entry in food_list:
        for allerg in a_entry:
            for ingr in ing_unique:
                if ingr not in i_entry:
                    df.loc[ingr, allerg] = 0
    return df


def count_no_allerg(df):
    no_allerg = list(df[df.sum(axis=1) == 0].index)
    count = 0
    for i_entry, a_entry in food_list:
        for ingr in i_entry:
            if ingr in no_allerg:
                count += 1
    return count

with open('input/day21.txt', 'r') as f:
    data =  f.read().split('\n')

food_list = parse_data(data)
df = return_allerg_df(food_list)


print(f'Part 1: {count_no_allerg(df)}')




df_allerg = df[df.sum(axis=1) == 0].index






