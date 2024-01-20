
# build a tree based on the map and count all nodes
# 64 steps, 1 -> 4 -> 16 -> 64 -> ...


data = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
"""

with open("../inputs/021.txt", "r") as fp: 
    data = fp.read()

example_map = [[c for c in line] for line in data.split("\n")]

start = None
for row, line in enumerate(example_map):
    for col, c in enumerate(line): 
        if c == 'S':
            start = (row, col, 'S')

assert start is not None
positions = [start]
tree = {start: set()} 
steps = 0

def get_height(node: tuple):
    if node not in tree:
        return 0
    if len(tree[node]) == 0:
        return 0 
    return max([get_height(adj) for adj in tree[node]]) + 1

steps = 0 
while True:
    steps += 1 
    new_positions = [] 
    while positions:
        row, col, val = positions.pop()
        
        up = example_map[row - 1][col] if row-1 >= 0 else None
        down = example_map[row + 1][col] if row+1 < len(example_map[0]) - 1 else None 
        left = example_map[row][col - 1] if col-1 >= 0 else None
        right = example_map[row][col + 1] if col+1 < len(example_map) - 1 else None
        
        #if (row, col, val) not in tree:
        #    tree[(row, col, val, height)] = set() 

        if up == '.' or up == 'S': 
            new_positions.append((row-1, col, up))
        if down == '.' or down == 'S':
            new_positions.append((row+1, col, down))
        if left == '.' or left == 'S':
            new_positions.append((row, col-1, left))
        if right == '.' or right == 'S':
            new_positions.append((row, col+1, right))

    positions = list(set(new_positions))
    if steps == 64: 
        break 

# print(positions)
print(len(positions))
# for pos in positions: 
#     row, col, val = pos 
#     example_map[row][col] = "O"

# for row in example_map: 
#     print(''.join(row))