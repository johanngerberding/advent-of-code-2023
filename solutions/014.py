import tqdm

# for every line, stops are 0 + the row of #
# for every col you go from 0 -> end and check whether the piece can move up or not

# directions: 
# 0 -> north
# 3 -> east 
# 2 -> south 
# 1 -> west

class Grid:
    def __init__(self, inp: str):
        self.grid = [[c for c in el] for el in inp.split("\n")]
        self.memory = {''.join([''.join(row) for row in self.grid]): 0} 
    
    def __repr__(self):
        rows = [''.join(row) for row in self.grid] 
        out = "" 
        for row in rows:
            out += (row + "\n")
        return out 

    def transform(self, direction: int):
        transformed = self.grid.copy() 
        # north -> col operations 
        if direction == 0:
            cols = [] 
            for col in range(len(self.grid[0])): 
                column = "" 
                for row in range(len(self.grid)):
                    column += self.grid[row][col]

                subparts = column.split("#")
                subparts = [''.join(sorted(el, reverse=True)) for el in subparts] 
                new_column = '#'.join(subparts)
                cols.append(new_column)
            
            for row in range(len(self.grid)):
                for col in range(len(self.grid[0])):
                    transformed[row][col] = cols[col][row] 
            

        
        # east -> row operations
        elif direction == 3:
            rows = []
            for r in self.grid:
                row = ''.join(r)

                subparts = row.split("#")
                subparts = [''.join(sorted(el)) for el in subparts] 
                new_row = '#'.join(subparts)
                rows.append(new_row)
            
            for row in range(len(self.grid)):
                for col in range(len(self.grid[0])):
                    transformed[row][col] = rows[row][col] 

        # south -> col operations
        elif direction == 2:
            cols = [] 
            for col in range(len(self.grid[0])): 
                column = "" 
                for row in range(len(self.grid)):
                    column += self.grid[row][col]

                subparts = column.split("#")
                subparts = [''.join(sorted(el)) for el in subparts] 
                new_column = '#'.join(subparts)
                cols.append(new_column)
            
            for row in range(len(self.grid)):
                for col in range(len(self.grid[0])):
                    transformed[row][col] = cols[col][row] 
        # west -> row operations
        elif direction == 1:
            rows = []
            for r in self.grid:
                row = ''.join(r)

                subparts = row.split("#")
                subparts = [''.join(sorted(el, reverse=True)) for el in subparts] 
                new_row = '#'.join(subparts)
                rows.append(new_row)
            
            for row in range(len(self.grid)):
                for col in range(len(self.grid[0])):
                    transformed[row][col] = rows[row][col] 
        else: 
            raise ValueError("Please give a valid direction value.")
    
        return transformed
    
    def load(self) -> int: 
        result = 0 
        scores = [i + 1 for i in range(len(self.grid))][::-1]
        for score, row in zip(scores, self.grid):
            result += sum([1 for el in row if el == 'O']) * score 
        return result

    def cycle(self, reps: int): 
        for i in range(reps): 
            for k in range(4):
                transformed = self.transform(k)
                grid = ''.join([''.join(row) for row in self.grid])
                if grid not in self.memory:
                    self.memory[grid] = i * 4 + k + 1
                    self.grid = transformed 
                else: 
                    pos = self.memory[grid] 
                    curr = i * 4 + k + 1 
                    pattern = curr - pos 
                    rest = reps * 4 - pos 
                    mod = rest % pattern 
                    for _ in range(mod):
                        transformed = self.transform(k)
                        self.grid = transformed 
                        if k <= 2:
                            k += 1
                        else: 
                            k = 0 
                    return 

example = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""

grid = Grid(example)

grid.cycle(1_000_000_000)
print(grid)

score = grid.load()
print(f"example part 2 -> {score}")

with open("../inputs/014.txt", "r") as fp:
    data = fp.read()

grid = Grid(data)
grid.cycle(1_000_000_000)
score = grid.load()
print(f"part 2: {score}")