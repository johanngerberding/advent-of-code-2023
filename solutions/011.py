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

expanded = expand(example)
galaxies = get_galaxies(expanded)
pairs = list(combinations(galaxies, 2))

grid = create_grid(expanded)

print(pairs)
print(len(pairs))
