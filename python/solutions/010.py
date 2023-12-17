from collections import defaultdict


def get_connections(lines: list, row: int, col: int) -> list: 
    adjs = [] 
    char = lines[row][col]
    if char != '.':
        if char == 'S':
            if row - 1 >= 0:
                above = lines[row - 1][col]
                if above in "7F|S": 
                    adjs.append(((row - 1), col))  
            if row + 1 < len(lines):
                below = lines[row + 1][col]
                if below in "LJ|S": 
                    adjs.append(((row + 1), col))
            if col - 1 >= 0:
                left = lines[row][col - 1]
                if left in "-J7S":
                    adjs.append((row, (col - 1)))
            if col + 1 < len(lines[row]):
                right = lines[row][col + 1]
                if right in "-J7S": 
                    adjs.append((row, (col + 1)))
        if char == '|':
            if row - 1 >= 0:
                above = lines[row - 1][col]
                if above in "7F|S": 
                    adjs.append(((row - 1), col))  
            if row + 1 < len(lines):
                below = lines[row + 1][col]
                if below in "LJ|S": 
                    adjs.append(((row + 1), col))
        elif char == '-':
            if col - 1 >= 0:
                left = lines[row][col - 1]
                if left in "-J7S":
                    adjs.append((row, (col - 1)))
            if col + 1 < len(lines[row]):
                right = lines[row][col + 1]
                if right in "-J7S": 
                    adjs.append((row, (col + 1))) 
        elif char == 'L':
            if row - 1 >= 0:
                above = lines[row - 1][col]
                if above in "7F|S":
                    adjs.append(((row - 1), col))
            if col + 1 < len(lines[row]):
                right = lines[row][col + 1]
                if right in "-J7S": 
                    adjs.append((row, (col + 1)))
        elif char == 'J':
            if row - 1 >= 0:
                below = lines[row - 1][col] 
                if below in "LJ|S": 
                    adjs.append(((row - 1), col))
            if col - 1 >= 0:
                left = lines[row][col - 1]
                if left in "-J7S": 
                    adjs.append((row, (col - 1)))
        elif char == '7':
            if row + 1 < len(lines):
                below = lines[row + 1][col] 
                if below in "LJ|S": 
                    adjs.append(((row + 1), col))
            if col - 1 >= 0:
                above = lines[row][col - 1] 
                if above in "7F|S": 
                    adjs.append((row, (col - 1)))
        elif char == 'F':
            if row + 1 < len(lines):
                below = lines[row + 1][col]
                if below in "LJ|S": 
                    adjs.append(((row + 1), col))
            if col + 1 < len(lines[row]):
                right = lines[row][col + 1]
                if right in "-J7S": 
                    adjs.append((row, (col + 1)))
    return adjs 

def parse(inp: str) -> tuple:
    graph = defaultdict(list) 
    lines = inp.split("\n")
    start = None 
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if lines[row][col] == 'S':
                start = (row, col) 
            if lines[row][col] != '.': 
                graph[(row, col)] = get_connections(lines, row, col)                
    
    assert start is not None 
    return graph, start

def find_circle(graph: defaultdict, start: tuple) -> set | None:
    visited = set()
    stack = [(start, None)]  # (node, parent)
    parent_map = {start: None}
    
    while stack:
        current, parent = stack.pop()

        if current in visited:
            # Found a circle
            circle_nodes = set()
            node = parent

            while node != current and node is not None:
                circle_nodes.add(node)
                node = parent_map[node]

            circle_nodes.add(current)
            return circle_nodes

        visited.add(current)

        for neighbor in graph[current]:
            if neighbor != parent:
                stack.append((neighbor, current))
                parent_map[neighbor] = current

    return None  # No circle found

def calculate_distances(graph: defaultdict, circle_nodes: set) -> dict:
    distances = {}

    for node in circle_nodes:
        distances[node] = {}
        for neighbor in graph[node]:
            if neighbor in circle_nodes:
                distances[node][neighbor] = 1  

    dists = {k: len(v) for k, v in distances.items()} 
    return dists 


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
print(graph)
circle_nodes = find_circle(graph, start)
print(circle_nodes)

if circle_nodes:
    print(f"Circle Nodes: {circle_nodes}")
    distances = calculate_distances(graph, circle_nodes)
    print("Distances:")
    for node in distances:
        print(f"{node}: {distances[node]}")
else:
    print("No circle found.")
