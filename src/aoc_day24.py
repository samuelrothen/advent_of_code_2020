# Advent of Code Day 24


import re


def return_tiles(data):
    tiles = {}
    for line in data:
        path = re.findall(r'e|se|sw|w|nw|ne', line)
        x = 0
        y = 0
        for move in path:
            if move == 'e':
                x += 2
            elif move == 'se':
                x += 1
                y -= 1
            elif move == 'sw':
                x -= 1
                y -= 1
            elif move == 'w':
                x -= 2
            elif move == 'nw':
                x -= 1
                y += 1
            elif move == 'ne':
                x += 1
                y += 1
        tiles[(x, y)] = 1 - tiles.get((x, y), 0)
    return tiles


def count_black(tiles):
    n_black = 0
    for k, v in tiles.items():
        n_black += v
    return n_black


def get_neighbors(x, y):
    neighbors=[(x+2,y),
                 (x+1,y-1),
                 (x-1,y-1),
                 (x-2,y),
                 (x-1,y+1),
                 (x+1,y+1)]
    return neighbors


def count_neighbors(tiles, x, y):
    count = 0
    for nx, ny in get_neighbors(x, y):
        if tiles.get((nx, ny), 0) == 1:
            count += 1
    return count


def calc_day(tiles):
    for k in list(tiles):
        if tiles[k] == 0:
            del tiles[k]

    new_tiles = {}
    for key, kval in tiles.items():
        kx, ky = key
        for nx, ny in get_neighbors(kx, ky):
            if (nx, ny) not in new_tiles:
                n_neighbors = count_neighbors(tiles, nx, ny)
                if n_neighbors == 2:
                    new_tiles[(nx, ny)] = 1

            n_neighbors = count_neighbors(tiles, kx, ky)
            if 0 < n_neighbors <=2:
                new_tiles[(kx, ky)] = 1
    return new_tiles


with open('../input/day24.txt', 'r') as f:
    data =  f.read().split('\n')


tiles = return_tiles(data)

print(f'Part 1: {count_black(tiles)}')


for day in range(100):
    tiles = calc_day(tiles)

print(f'Part 2: {count_black(tiles)}')

