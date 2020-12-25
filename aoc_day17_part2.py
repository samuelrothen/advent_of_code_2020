# Advent of Code Day 17 - Part 2


def parse_cubes(data):
    cubes = {(i, j, 0, 0):data[i][j]
             for i in range(len(data))
             for j in range(len(data[0]))}
    return cubes


def cube_neighbors(c):
    neighbors = [(c[0]+x, c[1]+y, c[2]+z, c[3]+w) 
                 for x in range(-1, 2) 
                 for y in range(-1, 2) 
                 for z in range(-1, 2)
                 for w in range(-1, 2)
                 if not (x == 0 and y == 0 and z == 0 and w == 0)]
    return neighbors


def active_neighbor_count(cube_check, cubes):
    neighbors = cube_neighbors(cube_check)
    n_active = 0
    for neighbor in neighbors:
        if cubes.get(neighbor) == '#':
            n_active += 1
    return n_active


def cubes_next_cycle(cubes):
    new_cubes = {}
    for cube in cubes:
        n_active = active_neighbor_count(cube, cubes)
        if cubes[cube] == '#':
            neighbors = cube_neighbors(cube)
            if n_active == 2 or n_active == 3:
                new_cubes[cube] = '#'
            else:
                new_cubes[cube] = '.'
            for nb in neighbors:
                if nb not in cubes:
                    n_active_nb = active_neighbor_count(nb, cubes)
                    if n_active_nb == 3:
                        new_cubes[nb] = '#'
        elif cubes[cube] == '.':
            if n_active == 3:
                new_cubes[cube] = '#'
            else:
                new_cubes[cube] = '.'
    return new_cubes


def return_active_cubes(cubes, n_cycles):
    for cycle in range(n_cycles):
        cubes = cubes_next_cycle(cubes)
    return list(cubes.values()).count('#')


with open ('input/day17.txt', 'r') as f:
    data =  f.read().split('\n')

cubes = parse_cubes(data)

print(f'Part 2: {return_active_cubes(cubes, 6)}')
