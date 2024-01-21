import numpy as np

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
..........."""

data = """.................................
.....###.#......###.#......###.#.
.###.##..#..###.##..#..###.##..#.
..#.#...#....#.#...#....#.#...#..
....#.#........#.#........#.#....
.##...####..##...####..##...####.
.##..#...#..##..#...#..##..#...#.
.......##.........##.........##..
.##.#.####..##.#.####..##.#.####.
.##..##.##..##..##.##..##..##.##.
.................................
.................................
.....###.#......###.#......###.#.
.###.##..#..###.##..#..###.##..#.
..#.#...#....#.#...#....#.#...#..
....#.#........#.#........#.#....
.##...####..##..S####..##...####.
.##..#...#..##..#...#..##..#...#.
.......##.........##.........##..
.##.#.####..##.#.####..##.#.####.
.##..##.##..##..##.##..##..##.##.
.................................
.................................
.....###.#......###.#......###.#.
.###.##..#..###.##..#..###.##..#.
..#.#...#....#.#...#....#.#...#..
....#.#........#.#........#.#....
.##...####..##...####..##...####.
.##..#...#..##..#...#..##..#...#.
.......##.........##.........##..
.##.#.####..##.#.####..##.#.####.
.##..##.##..##..##.##..##..##.##.
................................."""

#with open("../inputs/021.txt", "r") as fp: 
#    data = fp.read()

example_map = [[c for c in line] for line in data.split("\n")]

start = None
for row, line in enumerate(example_map):
    for col, c in enumerate(line): 
        if c == 'S':
            start = (row, col, 'S', 0, 0)

assert start is not None
positions = [start]

steps = 0 
while True:
    steps += 1 
    new_positions = set() 
    while positions:
        # track the positions relative to 'S' ??? 
        row, col, val, rel_row, rel_col = positions.pop()

        if row - 1 >= 0:
            up_row = row - 1
            up_col = col 
            up = example_map[up_row][up_col]
        else: 
            up_row = len(example_map) - 1
            up_col = col
            up = example_map[up_row][up_col] 
        
        if row + 1 < len(example_map) - 1:
            down_row = row + 1
            down_col = col 
            down = example_map[down_row][down_col] 
        else: 
            down_row = 0 
            down_col = col
            down = example_map[down_row][down_col] 

        if col - 1 >= 0:
            left_row = row 
            left_col = col - 1
            left = example_map[left_row][left_col]        
        else: 
            left_row = row 
            left_col = len(example_map[0]) - 1
            left = example_map[left_row][left_col] 
        
        if col + 1 < len(example_map[0]) - 1:
            right_row = row 
            right_col = col + 1   
            right = example_map[right_row][right_col] 
        else: 
            right_row = row 
            right_col = 0
            right = example_map[right_row][right_col]

        if up == '.' or up == 'S': 
            new_positions.add((up_row, up_col, up, rel_row - 1, rel_col))
        if down == '.' or down == 'S':
            new_positions.add((down_row, down_col, down, rel_row + 1, rel_col))
        if left == '.' or left == 'S':
            new_positions.add((left_row, left_col, left, rel_row, rel_col - 1))
        if right == '.' or right == 'S':
            new_positions.add((right_row, right_col, right, rel_row, rel_col + 1))

    positions = list(new_positions)
    if steps == 50: 
        break 

print(len(positions))
# for pos in positions: 
#     row, col, val = pos 
#     example_map[row][col] = "O"

# for row in example_map: 
#     print(''.join(row))

model = np.polyfit(
    [6, 10, 50, 100, 500, 1000, 5000], 
    [16, 50, 1594, 6536, 167004, 668697, 16733044], 
    2,
)
predict = np.poly1d(model)
print(predict(26501365))