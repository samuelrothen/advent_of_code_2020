# Advent of Code Day 20


import numpy as np


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

tile = tiles[2411]


T = [tile,
     np.flip(tile, axis=0),
     np.flip(tile, axis=1),
     np.rot90(tile, k=1),
     np.flip(np.rot90(tile, k=1), axis=0),
     np.flip(np.rot90(tile, k=1), axis=1),
     np.rot90(tile, k=2),
     np.rot90(tile, k=3)]


E = [tile[0, :],
     tile[-1, :],
     tile[:, 0],
     tile[:, -1],
     np.flip(tile[0, :]),
     np.flip(tile[-1, :]),
     np.flip(tile[:, 0]),
     np.flip(tile[:, -1])]






print(f'Part 1: {0}')
