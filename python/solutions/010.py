from collections import defaultdict

# go through all the nodes and fill a defaultdict 
# get cycle in subgraph

def get_connections(lines: list, row: int, col: int) -> list: 
    adjs = [] 
    char = lines[row][col]
    if char != '.':
        if char == 'S':
            if row - 1 >= 0:
                above = lines[row - 1][col]
                if above in "7F|": 
                    adjs.append(((row - 1), col))  
            if row + 1 < len(lines):
                below = lines[row + 1][col]
                if below in "LJ|": 
                    adjs.append(((row + 1), col))
            if col - 1 >= 0:
                left = lines[row][col - 1]
                if left in "-J7":
                    adjs.append(((col - 1), row))
            if col + 1 < len(lines[row]):
                right = lines[row][col + 1]
                if right in "-J7": 
                    adjs.append(((col + 1), row))
        if char == '|':
            if row - 1 >= 0:
                above = lines[row - 1][col]
                if above in "7F|": 
                    adjs.append(((row - 1), col))  
            if row + 1 < len(lines):
                below = lines[row + 1][col]
                if below in "LJ|": 
                    adjs.append(((row + 1), col))
        elif char == '-':
            if col - 1 >= 0:
                left = lines[row][col - 1]
                if left in "-J7":
                    adjs.append(((col - 1), row))
            if col + 1 < len(lines[row]):
                right = lines[row][col + 1]
                if right in "-J7": 
                    adjs.append(((col + 1), row)) 
        elif char == 'L':
            if row - 1 >= 0:
                above = lines[row - 1][col]
                if above in "7F|":
                    adjs.append(((row - 1), col))
            if col + 1 < len(lines[row]):
                right = lines[row][col + 1]
                if right in "-J7": 
                    adjs.append(((col + 1), row))
        elif char == 'J':
            if row - 1 >= 0:
                below = lines[row - 1][col] 
                if below in "LJ|": 
                    adjs.append(((row - 1), col))
            if col - 1 >= 0:
                left = lines[row][col - 1]
                if left in "-J7": 
                    adjs.append(((col - 1), row))
        elif char == '7':
            if row + 1 < len(lines):
                below = lines[row + 1][col] 
                if below in "LJ|": 
                    adjs.append(((row + 1), col))
            if col - 1 >= 0:
                above = lines[row][col - 1] 
                if above in "7F|": 
                    adjs.append(((col - 1), row))
        elif char == 'F':
            if row + 1 < len(lines):
                below = lines[row + 1][col]
                if below in "LJ|": 
                    adjs.append(((row + 1), col))
            if col + 1 < len(lines[row]):
                right = lines[row][col + 1]
                if right in "-J7": 
                    adjs.append(((col + 1), row))
    return adjs 

def parse(inp: str) -> tuple:
    graph = defaultdict(list) 
    lines = inp.split("\n")
    start = None 
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if lines[row][col] == 'S':
                start = (row, col) 
            graph[(row, col)] = get_connections(lines, row, col)                
    
    assert start is not None 
    
    return graph, start

def cycle(graph: defaultdict, start: tuple):
    visited = defaultdict(bool)
    visited[start] = True  
    adjs = graph[start]
    
    for adj in adjs:
        pass


example1 = """.....
.S-7.
.|.|.
.L-J.
....."""

example2 = """..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""


graph, start = parse(example1)
print(start)
print(graph)
