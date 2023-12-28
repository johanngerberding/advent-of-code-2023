
dir_change = {
    "/": {0: 3, 1: 2, 2: 1, 3: 0}, 
    "\\": {0: 1, 1: 0, 2: 3, 3: 2},
    "-": {0: 0, 2: 2},
    "|": {1: 1, 3: 3},
}

def next_pos(curr: tuple, direction: int, max_col: int, max_row: int) -> tuple | None: 
    if direction == 0:
        pos = (curr[0], curr[1] + 1) if 0 <= curr[1] + 1 <= max_col else None
    elif direction == 1: 
        pos = (curr[0] + 1, curr[1]) if 0 <= curr[0] + 1 <= max_row else None
    elif direction == 2: 
        pos = (curr[0], curr[1] - 1) if 0 <= curr[1] - 1 <= max_col else None
    elif direction == 3:
        pos = (curr[0] - 1, curr[1]) if 0 <= curr[0] - 1 <= max_row else None
    else: 
        raise ValueError("Direction value wrong")
    if pos:
        return (pos[0], pos[1], direction) 
    return None

def solve(inp: str):
    grid = []
    example = inp.split("\n")
    for row in example: 
        grid.append([el for el in row])

    max_row = len(grid) - 1 
    max_col = len(grid[0]) - 1 
    visited = set()
    # direction 0 -> right, 1 -> down, 2 -> left, 3 -> up
    stack = [(0, 0, 0)]


    while len(stack) > 0:
        curr = stack.pop()
        val = grid[curr[0]][curr[1]]
        direction = int(curr[2]) 
        if curr in visited:
            continue
        visited.add(curr)

        if val == ".":
            n = next_pos(curr, direction, max_row, max_col)
            if n is not None:
                stack.append(n) 
        elif val == "/":
            direction = dir_change["/"].get(direction) 
            assert direction is not None 
            n = next_pos(curr, direction, max_col, max_row) 
            if n is not None:
                stack.append(n) 
        elif val == "\\":
            direction = dir_change["\\"][direction]
            n = next_pos(curr, direction, max_col, max_row)
            if n is not None: 
                stack.append(n) 
        elif val == "-":
            if direction not in dir_change["-"]:
                # split
                for el in [0, 2]:
                    n = next_pos(curr, el, max_col, max_row) 
                    if n is not None: 
                        stack.append(n) 
            else:
                n = next_pos(curr, direction, max_col, max_row)  
                if n is not None: 
                    stack.append(n) 
        elif val == "|":
            if direction not in dir_change["|"]:
                # split
                for el in [1, 3]:
                    n = next_pos(curr, el, max_col, max_row)
                    if n is not None: 
                        stack.append(n) 
            else: 
                n = next_pos(curr, direction, max_col, max_row)
                if n is not None: 
                    stack.append(n)


    positions = set()
    for x, y, _ in visited: 
        positions.add((x,y))
    print(len(positions))


example = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|...."""

solve(example)

with open("../inputs/016.txt", "r") as fp: 
    data = fp.read()

solve(data)