
# build a tree based on the map and count all nodes
# 64 steps, 1 -> 4 -> 16 -> 64 -> ...


example_map = """...........
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

example_map = [[c for c in line] for line in example_map.split("\n")]

start = None
for row, line in enumerate(example_map):
    for col, c in enumerate(line): 
        if c == 'S':
            start = (row, col, 'S')

assert start is not None
stack = [start]
tree = {start: set()} 
c = 0
visited = set()
goal = 6

def height(node: tuple):
    print(node)
    if len(tree[node]) == 0:
        return 0 
    return max([height(adj) for adj in tree[node]]) + 1

while stack:
    c += 1 
    row, col, val = stack.pop()
    visited.add((row, col, val))
    up = example_map[row - 1][col] if row-1 > 0 else None
    down = example_map[row + 1][col] if row+1 < len(example_map[0]) - 1 else None 
    left = example_map[row][col - 1] if col-1 > 0 else None
    right = example_map[row][col + 1] if col+1 < len(example_map) - 1 else None
    
    # print(up, down, left, right) 
    if (row, col, val) not in tree:
        tree[(row, col, val)] = set() 

    if up == '.' and (row-1, col, up) not in visited:
        stack.append((row-1, col, up))
        tree[(row, col, val)].add((row-1, col, up)) 
    if down == '.' and (row+1, col, down) not in visited:
        stack.append((row+1, col, down))
        tree[(row, col, val)].add((row+1, col, down))
    if left == '.' and (row, col-1, left) not in visited:
        stack.append((row, col-1, left))
        tree[(row, col, val)].add((row, col-1, left)) 
    if right == '.' and (row, col+1, right) not in visited:
        stack.append((row, col+1, right))
        tree[(row, col, val)].add((row, col+1, right))

    if height(start) == goal:
        break
    # print(len(stack))
    # print(stack) 
    # print(tree)
    # if c == 5: 
    #     break

print(len(tree))