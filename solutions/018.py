from shapely.geometry import Polygon, Point


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
    for el in dig_plan: 
        curr = coordinates[-1] 
        if el[0] == 'R': 
            n = (curr[0], curr[1] + el[1])        
        elif el[0] == 'L': 
            n = (curr[0], curr[1] - el[1])        
        elif el[0] == 'U': 
            n = (curr[0] - el[1], curr[1])        
        elif el[0] == 'D':
            n = (curr[0] + el[1], curr[1])        
        dist += el[1] 
        coordinates.append(n)

    assert coordinates[-1] == (0, 0)
    pgon = Polygon(coordinates)
    min_x = min([el[0] for el in coordinates])
    max_x = max([el[0] for el in coordinates])
    min_y = min([el[1] for el in coordinates]) 
    max_y = max([el[1] for el in coordinates])
    
    area = 0
    for x in range(min_x, max_x + 1): 
        for y in range(min_y, max_y + 1):
            if pgon.contains(Point(x, y)): 
                area += 1 
            
    print(area + dist)

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

dig_plan = parse(data)
solve(dig_plan=dig_plan, part2=False)

