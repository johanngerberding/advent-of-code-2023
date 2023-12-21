from itertools import combinations

def expand(galaxy: str) -> list: 
    rows = galaxy.split("\n")
    expand_rows = sorted([i for i, row in enumerate(rows) if len(set(row)) == 1])
    cols = [] 
    for col in range(len(rows[0])):
        cols.append([row[col] for row in rows]) 
    expand_cols = sorted([i for i, col in enumerate(cols) if len(set(col)) == 1])

    curr_galaxy = []
    for i, row in enumerate(rows):
        curr_galaxy.append(row) 
        if i in expand_rows:
            expand_rows.pop(0)
            curr_galaxy.append(''.join(['.' for _ in range(len(row))]))

    expanded_galaxy = []
    for i, row in enumerate(curr_galaxy): 
        nrow = row  
        for j, col in enumerate(expand_cols):
            nrow = nrow[:col + j] + '.' + nrow[col + j:]
        expanded_galaxy.append(nrow)

    return expanded_galaxy

def get_galaxies(expanded_galaxy: list) -> list: 
    galaxies = [] 
    for i, row in enumerate(expanded_galaxy):
        for j, el in enumerate(row): 
            if el == '#':
                galaxies.append((i, j)) 
    return galaxies 


def get_distance(pair: tuple) -> int: 
    initial, end = pair 
    row_diff = max(initial[0], end[0]) - min(initial[0], end[0])
    col_diff = max(initial[1], end[1]) - min(initial[1], end[1])
    return row_diff + col_diff 



def solve(inp: str) -> int:
    expanded = expand(inp)
    galaxies = get_galaxies(expanded)
    pairs = list(combinations(galaxies, 2))

    result = 0 
    for pair in pairs: 
        shortest_path = get_distance(pair) 
        result += shortest_path
    return result


example = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

example_result = solve(example)
print(f"Example result: {example_result}")

with open("../inputs/011.txt", "r") as fp: 
    data = fp.read()

part1 = solve(data)
print(f"Part 1: {part1}")
