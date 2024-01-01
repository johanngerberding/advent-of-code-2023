import heapq

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

with open("../inputs/017.txt", "r") as fp: 
    data = fp.read()

grid = [[el for el in row] for row in data.split("\n")]
R = len(grid)
C = len(grid[0])


def solve(part2):
    distances = {}
    heap = [(0, 0, 0, -1, -1)]

    while heap: 
        dist, r, c, dir_, indir = heapq.heappop(heap)
        if (r, c, dir_, indir) in distances:
            continue 
        distances[(r, c, dir_, indir)] = dist 
        for i, (dr, dc) in enumerate([[-1, 0], [0, 1], [1, 0], [0, -1]]):
            rr = r + dr 
            cc = c + dc 
            new_dir = i 
            new_indir = (1 if new_dir != dir_ else indir + 1)
            
            isnt_reverse = ((new_dir + 2) % 4 != dir_)
            
            is_valid_part1 = (new_indir <= 3) 
            is_valid_part2 = (new_indir <= 10 and (new_dir == dir_ or indir >= 4 or indir == -1))
            isvalid = (is_valid_part2 if part2 else is_valid_part1)

            if 0 <= rr < R and 0 <= cc < C and isnt_reverse and isvalid:
                cost = int(grid[rr][cc])
                if (rr, cc, new_dir, new_indir) in distances: 
                    continue 
                heapq.heappush(heap, (dist + cost, rr, cc, new_dir, new_indir))

    ans = 1e9 
    for (r, c, dir_, indir), v in distances.items():
        if r == R - 1 and c == C - 1 and (indir >= 4 or not part2):
            ans = min(ans, v)

    print(ans)

print(f"Part 1: ", end="")
solve(False)
print(f"Part 2: ", end="")
solve(True)
