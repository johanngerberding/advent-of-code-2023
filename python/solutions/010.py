from collections import defaultdict


# go through all the nodes and fill a defaultdict 
# get cycle in subgraph
class Node: 
    def __init__(self, pos: tuple, symbol: str, distance: int = 0, visited: bool = False):
        self.pos = pos 
        self.distance = distance
        self.symbol = symbol
        self.visited = visited
    
    def __repr__(self):
        return f"{self.symbol}: {self.pos} -> {self.distance} ({self.distance})"


def get_connections(lines: list, row: int, col: int) -> list: 
    adjs = [] 
    char = lines[row][col]
    if char != '.':
        if char == 'S':
            if row - 1 >= 0:
                above = lines[row - 1][col]
                if above in "7F|": 
                    adjs.append(Node(((row - 1), col), char))  
            if row + 1 < len(lines):
                below = lines[row + 1][col]
                if below in "LJ|": 
                    adjs.append(Node(((row + 1), col), char))
            if col - 1 >= 0:
                left = lines[row][col - 1]
                if left in "-J7":
                    adjs.append(Node(((col - 1), row), char))
            if col + 1 < len(lines[row]):
                right = lines[row][col + 1]
                if right in "-J7": 
                    adjs.append(Node(((col + 1), row), char))
        if char == '|':
            if row - 1 >= 0:
                above = lines[row - 1][col]
                if above in "7F|": 
                    adjs.append(Node(((row - 1), col), char))  
            if row + 1 < len(lines):
                below = lines[row + 1][col]
                if below in "LJ|": 
                    adjs.append(Node(((row + 1), col), char))
        elif char == '-':
            if col - 1 >= 0:
                left = lines[row][col - 1]
                if left in "-J7":
                    adjs.append(Node(((col - 1), row), char))
            if col + 1 < len(lines[row]):
                right = lines[row][col + 1]
                if right in "-J7": 
                    adjs.append(Node(((col + 1), row), char)) 
        elif char == 'L':
            if row - 1 >= 0:
                above = lines[row - 1][col]
                if above in "7F|":
                    adjs.append(Node(((row - 1), col), char))
            if col + 1 < len(lines[row]):
                right = lines[row][col + 1]
                if right in "-J7": 
                    adjs.append(Node(((col + 1), row), char))
        elif char == 'J':
            if row - 1 >= 0:
                below = lines[row - 1][col] 
                if below in "LJ|": 
                    adjs.append(Node(((row - 1), col), char))
            if col - 1 >= 0:
                left = lines[row][col - 1]
                if left in "-J7": 
                    adjs.append(Node(((col - 1), row), char))
        elif char == '7':
            if row + 1 < len(lines):
                below = lines[row + 1][col] 
                if below in "LJ|": 
                    adjs.append(Node(((row + 1), col), char))
            if col - 1 >= 0:
                above = lines[row][col - 1] 
                if above in "7F|": 
                    adjs.append(Node(((col - 1), row), char))
        elif char == 'F':
            if row + 1 < len(lines):
                below = lines[row + 1][col]
                if below in "LJ|": 
                    adjs.append(Node(((row + 1), col), char))
            if col + 1 < len(lines[row]):
                right = lines[row][col + 1]
                if right in "-J7": 
                    adjs.append(Node(((col + 1), row), char))
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


def dfs(graph: defaultdict, pos: tuple, start: tuple, step: int): 
    step += 1 
    graph[pos].visited = True 
    graph[pos].distance = step
    for el in graph: 
        if not graph[el].visited: 
            dfs(graph=graph, pos=el, start=start, step=step)
        elif el == start and step == 0:
            print("Found a cycle") 
            return graph
    return graph

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
distances = defaultdict(int)

graph = dfs(graph, start, start, -1)

for el in graph:
    print(el)