
def find_mirror(example: list) -> int:
    for row in range(1, len(example)):
        if example[row - 1] == example[row]:
            # print(f"Found two same rows: {row}") 
            up = ''.join(example[:row - 1][::-1])
            down = ''.join(example[row + 1:])
            if len(up) > len(down):
                if up.startswith(down): 
                    return row
            else: 
                if down.startswith(up):
                    return row
    return -1


def find_vertical(example: list) -> int:
    nexample = [] 
    for i in range(len(example[0])): 
        col = "" 
        for j in range(len(example)):
            col += example[j][i]
        nexample.append(col) 
    return find_mirror(nexample)


def solve(examples: list):
    result = 0
    for example in examples: 
        h = find_mirror(example)
        if not h > 0: 
            v = find_vertical(example)
            if v != -1: 
                result += v
            else: 
                raise ValueError("Problem") 
        else:  
            result += (h * 100) 

    print(f"Result: {result}")


example = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""

examples = example.split("\n\n")
examples = [example.split("\n") for example in examples]
print(f"Number of examples: {len(examples)}")
solve(examples)

with open("../inputs/013.txt", "r") as fp:
    data = fp.read()

data = data.split("\n\n")
data = [d.split("\n") for d in data]
print(f"Number of examples part 1: {len(data)}")

solve(data)