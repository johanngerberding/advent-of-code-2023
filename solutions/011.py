from itertools import combinations

def expand(galaxy: str) -> list: 
    rows = galaxy.split("\n")
    expand_rows = sorted([i for i, row in enumerate(rows) if len(set(row)) == 1])
    cols = [] 
    for col in range(len(rows[0])):
        cols.append([row[col] for row in rows]) 
    expand_cols = sorted([i for i, col in enumerate(cols) if len(set(col)) == 1])

    return rows, expand_rows, expand_cols

def get_galaxies(galaxy: list, expand_rows: list, expand_cols: list, expansion_factor: int) -> list: 
    galaxies = []
    for i, row in enumerate(galaxy):
        for j, el in enumerate(row): 
            if el == '#':
                add_rows = len([el for el in expand_rows if el < i]) * expansion_factor
                add_cols = len([el for el in expand_cols if el < j]) * expansion_factor 
                galaxies.append((i + add_rows, j + add_cols)) 
    
    return galaxies 


def get_distance(pair: tuple) -> int: 
    initial, end = pair 
    row_diff = max(initial[0], end[0]) - min(initial[0], end[0])
    col_diff = max(initial[1], end[1]) - min(initial[1], end[1])
    return row_diff + col_diff 



def solve(inp: str, expansion_factor: int) -> int:
    galaxy, expand_rows, expand_cols = expand(inp)
    galaxies = get_galaxies(galaxy, expand_rows, expand_cols, expansion_factor)
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

example_result = solve(example, expansion_factor=1)
print(f"Example result: {example_result}")

example_result_2 = solve(example, expansion_factor=9)
print(f"Example part 2: {example_result_2}")

with open("../inputs/011.txt", "r") as fp: 
    data = fp.read()

part1 = solve(data, expansion_factor=1)
print(f"Part 1: {part1}")

part2 = solve(data, expansion_factor=1_000_000 - 1)
print(f"Part 1: {part2}")
