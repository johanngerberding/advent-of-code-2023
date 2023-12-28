from collections import defaultdict


def get_adjs(pos: tuple, max_row: int, max_col: int) -> list:
    up = (pos[0] - 1, pos[1]) if pos[0] - 1 >= 0 else None 
    down = (pos[0] + 1, pos[1]) if pos[0] + 1 <= max_row else None 
    right = (pos[0], pos[1] + 1) if pos[1] + 1 <= max_col else None 
    left = (pos[0], pos[1] - 1) if pos[1] - 1 >= 0 else None  
    result = []
    if up:
        result += up 
    if down: 
        result += down
    if right: 
        result += right 
    if left: 
        result += left 
    return result 


example = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""

grid = [[el for el in row] for row in example.split("\n")]
start = (0,0)
max_row = len(grid) - 1
max_col = len(grid[0]) - 1
end = (len(grid) - 1, len(grid[0]) - 1)
print(f"{start} -> {end}")

visited = set()
distances = defaultdict(list) 
stack = [start]

while len(stack) > 0:
    node = stack.pop()
    if node in visited:
        continue  
    visited.add(node)



for row in range(len(grid)):
    for col in range(len(grid[0])):
        ...


