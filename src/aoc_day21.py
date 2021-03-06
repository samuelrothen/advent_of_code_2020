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

with open('../input/day21.txt', 'r') as f:
    data =  f.read().split('\n')

food_list = parse_data(data)
df = return_allerg_df(food_list)


print(f'Part 1: {count_no_allerg(df)}')


ing_unique, alg_unique = return_unique(food_list)
df_allerg = df[df.sum(axis=1) > 0]
dict_allerg = {}


while len(dict_allerg) < len(alg_unique):
    s_allerg = df_allerg.sum(axis = 0)
    for a in s_allerg[s_allerg == 1].index:
        ing = df_allerg[a][df_allerg[a] == 1].index.values[0]
        dict_allerg[a] = ing
        df_allerg = df_allerg.drop(a, axis = 1)
        df_allerg = df_allerg.drop(ing, axis = 0)
    
    s_ingr = df_allerg.sum(axis = 1)
    for ing in s_ingr[s_ingr == 1].index:
        a = df_allerg.loc[ing][df_allerg.loc[ing] == 1].index.values[0]
        dict_allerg[a] = ing
        df_allerg = df_allerg.drop(a, axis = 1)
        df_allerg = df_allerg.drop(ing, axis = 0)

ing_list=''
for a, ing in sorted(dict_allerg.items()):
    ing_list = ing_list + ing + ','
ing_list = ing_list[:-1]


print(f'Part 2: {ing_list}')
