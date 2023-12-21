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


def create_grid(expanded: list) -> dict: 
    grid = {} 
    
    for r, row in enumerate(expanded): 
        for c in range(len(row)): 
            if not (r, c) in grid: 
                grid[(r, c)] = []

            grid[(r, c)].append((r - 1, c)) if r > 0 else None
            grid[(r, c)].append((r + 1, c)) if r < (len(expanded) - 1) else None
            grid[(r, c)].append((r, c + 1)) if c < len(row) - 1 else None
            grid[(r, c)].append((r, c - 1)) if c > 0 else None

    return grid     

def dijsktra(grid: dict, initial: tuple, end: tuple) -> int: 
    shortest_paths = {initial: (None, 0)}
    current_node = initial 
    visited = set()

    while current_node != end: 
        visited.add(current_node)
        adjs = grid[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for adj in adjs: 
            weight = 1 + weight_to_current_node 
            if adj not in shortest_paths: 
                shortest_paths[adj]  = (current_node, weight) 
            else: 
                current_shortest_weight = shortest_paths[adj][1] 
                if current_shortest_weight > weight: 
                    shortest_paths[adj] = (current_node, weight) 

        next_adjs = {node: shortest_paths[node] for node in shortest_paths if node not in visited} 

        if not next_adjs: 
            return -1

        current_node = min(next_adjs, key=lambda k: next_adjs[k][1])

    # work back through adjs in shortest path
    path = [] 
    while current_node is not None: 
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node

    # reverse path 
    # path = path[::-1]
    return len(path) - 1


def solve(inp: str) -> int:
    expanded = expand(inp)
    galaxies = get_galaxies(expanded)
    pairs = list(combinations(galaxies, 2))
    grid = create_grid(expanded)

    result = 0 
    for pair in pairs: 
        shortest_path = dijsktra(grid, pair[0], pair[1])
        if shortest_path == -1: 
            print(f"We have a problem, no path between {pair[0]} and {pair[1]}")
            raise ValueError
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
