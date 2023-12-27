

# for every line, stops are 0 + the row of #
# for every col you go from 0 -> end and check whether the piece can move up or not

# directions: 
# 0 -> north
# 1 -> east 
# 2 -> south 
# 3 -> west

class Grid:
    def __init__(self, inp: str):
        self.grid = [[c for c in el] for el in inp.split("\n")]

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
        elif direction == 1:
            ...
        # south -> col operations
        elif direction == 2:
            ...
        # west -> row operations
        elif direction == 3:
            ...
        else: 
            raise ValueError("Please give a valid direction value.")
    
        self.grid = transformed
    
    def load(self) -> int: 
        result = 0 
        scores = [i + 1 for i in range(len(self.grid))][::-1]
        for score, row in zip(scores, self.grid):
            result += sum([1 for el in row if el == 'O']) * score 
        return result

# def parse(inp: str):
#     rows = inp.split("\n") 
#     cols = []
#     # get col values
#     for c in range(len(rows[0])):    
#         col = "" 
#         for i in range(len(rows)):
#             col += rows[i][c]
#         cols.append(col)

#     ...



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

print(grid.grid)
grid.transform(0)
print(grid.grid)
score = grid.load()
print(f"example -> {score}")

with open("../inputs/014.txt", "r") as fp:
    data = fp.read()

grid = Grid(data)
grid.transform(0)
part1 = grid.load()
print(f"part1: {part1}")