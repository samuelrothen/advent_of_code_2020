# Advent of Code Day 24

import re

data = '''sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew'''.split('\n')


with open('input/day24.txt', 'r') as f:
    data =  f.read().split('\n')


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


n_black = 0
for k, v in tiles.items():
    n_black += v







