
def get_adjs(grid: list, pos: tuple) -> list:
    up = (pos[0] - 1, pos[1], int(grid[pos[0] - 1][pos[1]])) if pos[0] - 1 >= 0 else None 
    down = (pos[0] + 1, pos[1], int(grid[pos[0] + 1][pos[1]])) if pos[0] + 1 <= (len(grid) - 1) else None 
    right = (pos[0], pos[1] + 1, int(grid[pos[0]][pos[1] + 1])) if pos[1] + 1 <= (len(grid[0]) - 1) else None 
    left = (pos[0], pos[1] - 1, int(grid[pos[0]][pos[1] - 1])) if pos[1] - 1 >= 0 else None  
    result = []
    result.append(up) if up is not None else None
    result.append(down) if down is not None else None
    result.append(right) if right is not None else None
    result.append(left) if left is not None else None
    return result 

PATHS = []

def get_all_paths_util(graph: dict, u: tuple, d: tuple, visited: dict, path: list):
    # Mark the current node as visited and store in path 
    visited[u]= True 
    path.append(u)

    # If current vertex is same as destination, then print
    # current path[]
    if u == d:
        print(len(path))
        PATHS.append(path)
    else:
        # If current vertex is not destination
        # Recur for all the vertices adjacent to this vertex
        for adj in graph[u]:
            # constraint 
            if len(path) >= 4:
                last_3_rows = []
                last_3_cols = [] 
                for i in range(-2, -5, -1): 
                    row, col, _ = path[i] 
                    last_3_rows.append(row)
                    last_3_cols.append(col)
                if len(set(last_3_cols)) == 1: 
                    # same col 
                    val = last_3_cols[0] 
                    if adj[1] == val:
                        continue 
                elif len(set(last_3_rows)) == 1:
                    # same row 
                    val = last_3_rows[0]
                    if adj[0] == val: 
                        continue

            if visited[adj] is False:
                get_all_paths_util(graph, adj, d, visited, path)
                    
    # Remove current vertex from path[] and mark it as unvisited
    path.pop()
    visited[u]= False


# Prints all paths from 's' to 'd'
def get_all_paths(graph: dict, s: tuple, d: tuple):

    # Mark all the vertices as not visited
    visited = {node: False for node in graph} 

    # Create an array to store paths
    path = []
    # Call the recursive helper function to print all paths
    get_all_paths_util(graph, s, d, visited, path)

def find_all_paths(graph: dict, start: tuple, end: tuple, path=None, visited=None):
    if visited is None:
        visited = set()
    if path is None:
        path = [] 
    visited.add(start) 
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in visited:
            new_paths = find_all_paths(graph, node, end, path, visited)
            for new_path in new_paths:
                paths.append(new_path)
    visited.remove(start) 
    return paths


example = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""

grid = [[el for el in row] for row in example.split("\n")]
start = (0,0,int(grid[0][0])) # row, col, cost, path 
end = (len(grid) - 1, len(grid[0]) - 1, int(grid[len(grid) - 1][len(grid[0]) - 1]))
print(f"{start} -> {end}")

graph = {}
for row in range(len(grid)):
    for col in range(len(grid[0])):
        node = (row, col, int(grid[row][col]))
        adjs = get_adjs(grid, node)
        graph[node] = adjs

assert end in graph 
assert start in graph

get_all_paths(graph, start, end)
print(len(PATHS))
print(PATHS[0])

"""
unvisited_nodes = set() 
distances = {node: 1000000 for node in unvisited_nodes} 
distances[start] = 0 
previous = {}

while unvisited_nodes:
    current_min_node = None
    for node in unvisited_nodes: 
        if current_min_node is None:
            current_min_node = node
        elif distances[node] < distances[current_min_node]:
            current_min_node = node

    assert current_min_node
    # [up, right, down, left]
    neighbors = get_adjs(grid, current_min_node)

    # constraint -> take out the direction which was executed the last three times
    last_3 = []
    x0, y0, _ = current_min_node 
    for _ in range(3):
        if previous.get(current_min_node):
            x1, y1, _ = previous[current_min_node] 
            if x0 == x1: 
                y = y0 - y1 
                last_3.append(0) if y == 1 else last_3.append(2)
            else: 
                x = x0 - x1
                last_3.append(1) if x == -1 else last_3.append(3)

    if len(set(last_3)) == 1:
        print(f"Found 3 consecutive moves: {last_3}") 
        neighbors[last_3[0]] = None 
        print(neighbors)

    for neighbor in neighbors:
        if neighbor: 
            temp_distance = distances[current_min_node] + neighbor[2] 
            if neighbor in distances:
                if temp_distance < distances[neighbor]: 
                    distances[neighbor] = temp_distance 
            else: 
                distances[neighbor] = temp_distance
            previous[neighbor] = current_min_node

    unvisited_nodes.remove(current_min_node)


print(distances[end])


path = []
node = end 

while node != start:
    path.append(node)
    node = previous[node]

# Add the start node manually
path.append(start)

print("We found the following best path with a value of {}.".format(distances[end]))
print(" -> ".join(reversed(path)))
"""

