from shapely.geometry import Polygon, Point
from collections import defaultdict
from itertools import groupby
from operator import itemgetter 


def reduce(cols: list) -> list: 
    cols.sort() 
    new_ranges = [] 

    left, right = cols[0]
    for col in cols[1:]:
        next_left, next_right = col
        if right + 1 < next_left: 
            new_ranges.append((left, right)) 
            left, right = col  
        else: 
            right = max(right, next_right) 

    new_ranges.append((left, right)) 
    return new_ranges


def parse(inp: str) -> list:
    dig_plan = inp.split("\n")
    dig_plan = [el.split(" ") for el in dig_plan]
    dig_plan = [[el[0], int(el[1]), el[2][1:-1]] for el in dig_plan]

    return dig_plan


def solve(dig_plan: list, part2: bool): 
    if part2: 
        num2dir = {0: 'R', 1: 'D', 2: 'L', 3: 'U'}
        correct_dig_plan = [[num2dir[int(el[2][-1])], int(el[2][1:-1], 16)] for el in dig_plan] 
        dig_plan = correct_dig_plan 

    # list of coordinates 
    coordinates = [(0, 0)]
    dist = 0 
    rows = defaultdict(set) 

    for el in dig_plan: 
        curr = coordinates[-1] 
        if el[0] == 'R': 
            n = (curr[0], curr[1] + el[1]) 
            # for c in range(curr[0], n[1] + 1):
                # rows[curr[0]].add(c)
            rows[n[0]].add((curr[1], n[1])) 
        elif el[0] == 'L': 
            n = (curr[0], curr[1] - el[1])
            # for c in range(curr[0], n[1] - 1, -1):        
                # rows[curr[0]].add(c)
            rows[n[0]].add((curr[1], n[1]))
        elif el[0] == 'U': 
            n = (curr[0] - el[1], curr[1])        
            for r in range(curr[0], n[0] - 1, -1):
                rows[r].add((curr[1], curr[1]))
        elif el[0] == 'D':
            n = (curr[0] + el[1], curr[1])        
            for r in range(curr[0], n[0] + 1):
                rows[r].add((curr[1], curr[1]))
        dist += el[1] 
        coordinates.append(n)

    assert coordinates[-1] == (0, 0)
    pgon = Polygon(coordinates)
    min_x = min([el[0] for el in coordinates])
    max_x = max([el[0] for el in coordinates])
    min_y = min([el[1] for el in coordinates]) 
    max_y = max([el[1] for el in coordinates])
    # print(rows) 
    area = 0
    # this is the problem for part 2 
    # this could be done much smarter  
    # reduce consecutive blocks to start + end points
    for x in range(min_x, max_x + 1):
        row_area = 0 
        cols = sorted(list(rows[x]))
        correct_cols = [
            (min([el[0], el[1]]), max([el[0], el[1]])) for el in cols
        ] 
        correct_cols = reduce(correct_cols) 
        
        # for i in range(1, len(correct_cols)):
        #     row_area += correct_cols[i][0] - correct_cols[i-1][1]
        #     if row_area != 0: 
        #         row_area += 1 
        if len(correct_cols) == 1: 
            row_area += (correct_cols[0][1] + 1 - correct_cols[0][0]) 
        else:
            for col in correct_cols: 
                if col[0] != col[1]: 
                    row_area += (col[1] - col[0])
            for i in range(1, len(correct_cols)): 
                row_area += (correct_cols[i][0] + 1 - correct_cols[i - 1][1])
        # assert len(cols) % 2 == 0
        # for y in range(min_y, max_y + 1):
        #     if pgon.contains(Point(x, y)): 
        #         area += 1
        # print(f"row {x}: {correct_cols} -> {row_area}") 
        area += row_area 
    print(area)

example = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""

dig_plan_example = parse(example)
solve(dig_plan_example, False)
solve(dig_plan_example, True)

with open("../inputs/018.txt", 'r') as fp: 
    data = fp.read()

# hdig_plan = parse(data)
# solve(dig_plan=dig_plan, part2=False)

