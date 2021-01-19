# Advent of Code Day 20 - Part 1


import numpy as np
from itertools import product

def parse_tiles(data):
    tiles = {}
    for tile in data:
        num, pattern = tile.split('Tile ')[1].split(':\n')
        pattern=pattern.replace('.', '0').replace('#', '1').split('\n')
        tile_array = np.array([[int(c) for c in list(row)] for row in pattern])
        tiles[int(num)] = tile_array
    return tiles


with open('input/day20.txt', 'r') as f:
    data =  f.read().split('\n\n')


tiles = parse_tiles(data)

tiles_T = {}
edges_T = {}

for num, tile in tiles.items():
    T = [tile,
         np.flip(tile, axis = 0),
         np.flip(tile, axis = 1),
         np.rot90(tile, k = 1),
         np.flip(np.rot90(tile, k = 1), axis = 0),
         np.flip(np.rot90(tile, k = 1), axis = 1),
         np.rot90(tile, k = 2),
         np.rot90(tile, k = 3)]

    E = [tile[0, :],
         tile[-1, :],
         tile[:, 0],
         tile[:, -1],
         np.flip(tile[0, :]),
         np.flip(tile[-1, :]),
         np.flip(tile[:, 0]),
         np.flip(tile[:, -1])]

    tiles_T[num] = T  
    edges_T[num] = E

n_matches = {num: 0 for num in tiles}
for (num1, edges1), (num2, edges2) in product(edges_T.items(), edges_T.items()):
    if num1 == num2:
        continue
    for e1, e2 in product(edges1, edges2[:4]):
        if abs((e1 - e2)).sum() == 0:
            n_matches[num1] += 1

result = 1
for num, m in n_matches.items():
    if m == 2:
        result *= num



print(f'Part 1: {result}')
