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
corners = []
for num, m in n_matches.items():
    if m == 2:
        result *= num
        corners.append(num)


print(f'Part 1: {result}')



#%%


# for y, x in product(range(12), range(12)):
    # print(f'x:{x} y:{y}')


size = int(len(tiles_T) ** 0.5)
pic = np.zeros((8 * size, 8 * size))


remaining_tiles = list(tiles_T.keys())
corner = corners[0]
remaining_tiles.remove(corner)

c_ori = 0
pic[:8, :8] = tiles_T[corner][c_ori][1:-1, 1:-1]

bot_edge = tiles_T[corner][c_ori][-1, :]
rgt_edge = tiles_T[corner][c_ori][:, -1]

for y, x in product(range(size), range(size)):
    if x == 0 and y == 0:
        continue
    if x > 0:
        found_match = False
        for rem in remaining_tiles:
            for ori_T in tiles_T[rem]:
                if abs((ori_T[:, 0] - rgt_edge)).sum() == 0:
                    print('Match')
                    remaining_tiles.remove(rem)
                    pic_part = ori_T[1:-1, 1:-1]
                    pic[y*8:(y+1)*8, x*8:(x+1)*8] = pic_part
                    rgt_edge = ori_T[:, -1]
                    found_match = True
                    break
            if found_match:
                break

    if y > 0 and x == 0:
        found_match = False
        for rem in remaining_tiles:
            for ori_T in tiles_T[rem]:
                if abs((ori_T[0, :] - bot_edge)).sum() == 0:
                    print('Match')
                    remaining_tiles.remove(rem)
                    pic_part = ori_T[1:-1, 1:-1]
                    pic[y*8:(y+1)*8, x*8:(x+1)*8] = pic_part
                    bot_edge = ori_T[-1, :]
                    rgt_edge = ori_T[:, -1]
                    found_match = True
                    break
            if found_match:
                break

monster = '''                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''

monster = monster.replace('#', '1').replace(' ','0')
monster = np.array([[int(c) for c in list(row)] for row in monster.split('\n')])


