
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

#with open("../inputs/021.txt", "r") as fp: 
#    data = fp.read()

example_map = [[c for c in line] for line in data.split("\n")]

start = None
for row, line in enumerate(example_map):
    for col, c in enumerate(line): 
        if c == 'S':
            start = (row, col, 'S', 0)

assert start is not None
stack = [start]
tree = {start: set()} 
c = 0
visited = set()
steps = 0

def get_height(node: tuple):
    if node not in tree:
        return 0
    if len(tree[node]) == 0:
        return 0 
    return max([get_height(adj) for adj in tree[node]]) + 1

while stack: 
    row, col, val, height = stack.pop()
    visited.add((row, col, val))
    up = example_map[row - 1][col] if row-1 > 0 else None
    down = example_map[row + 1][col] if row+1 < len(example_map[0]) - 1 else None 
    left = example_map[row][col - 1] if col-1 > 0 else None
    right = example_map[row][col + 1] if col+1 < len(example_map) - 1 else None
    
    # print(up, down, left, right) 
    if (row, col, val) not in tree:
        tree[(row, col, val, height)] = set() 

    if up == '.' and (row-1, col, up) not in visited: 
        stack.append((row-1, col, up, height + 1))
        tree[(row, col, val, height)].add((row-1, col, up, height + 1))  
    if down == '.' and (row+1, col, down) not in visited:
        stack.append((row+1, col, down, height + 1))
        tree[(row, col, val, height)].add((row+1, col, down, height + 1))
    if left == '.' and (row, col-1, left) not in visited:
        stack.append((row, col-1, left, height + 1))
        tree[(row, col, val, height)].add((row, col-1, left, height + 1)) 
    if right == '.' and (row, col+1, right) not in visited:
        stack.append((row, col+1, right, height + 1))
        tree[(row, col, val, height)].add((row, col+1, right, height + 1))

    
print(len(visited))
res = 0 
for k, v in tree.items():
    res += len([el for el in v if el[3] < 6])

print(res -1)