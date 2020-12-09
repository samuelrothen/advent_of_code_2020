# Advent of Code Day 3


def check_trees(tree_map, n_steps_r, n_steps_d):
    x = 0
    n_trees = 0
    map_border = len(tree_map[0])
    for y in range(0, len(tree_map)-1, n_steps_d):
        x = (x + n_steps_r) % map_border
        field = tree_map[n_steps_d + y][x]
        if field == '#':
            n_trees += 1
    return n_trees


with open ('input/day3.csv', 'r') as f:
    tree_map = f.read().splitlines()


# Right 1, down 1
r1_d1 = check_trees(tree_map, 1, 1)
# Right 3, down 1 (Part 1)
r3_d1 = check_trees(tree_map, 3, 1)
# Right 5, down 1
r5_d1 = check_trees(tree_map, 5, 1)
# Right 7, down 1
r7_d1 = check_trees(tree_map, 7, 1)
# Right 1, down 2
r1_d2 = check_trees(tree_map, 1, 2)


print(f'Part 1: {r3_d1}')
print(f'Part 2: {r1_d1 * r3_d1 * r5_d1 * r7_d1 * r1_d2}')