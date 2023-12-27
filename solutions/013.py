
def count_diff_symbols(string1: str, string2: str) -> int:
    count = 0
    min_len = min(len(string1), len(string2))

    for i in range(min_len):
        if string1[i] != string2[i]:
            count += 1

    # If the strings have different lengths, consider the remaining characters as differences
    count += abs(len(string1) - len(string2))
    return count


def find_mirror2(example: list) -> int:
    for row in range(1, len(example)):
        diff = count_diff_symbols(example[row - 1], example[row]) 
        if diff == 0:
            up = ''.join(example[:row - 1][::-1])
            down = ''.join(example[row + 1:])
            if len(up) > len(down):
                up = up[:len(down)]
            else: 
                down = down[:len(up)] 
            diff = count_diff_symbols(up, down) 
            if diff == 1:
                return row
        if diff == 1: 
            up = ''.join(example[:row - 1][::-1])
            down = ''.join(example[row + 1:])
            if len(up) > len(down):
                up = up[:len(down)]
            else: 
                down = down[:len(up)] 
            diff = count_diff_symbols(up, down) 
            if diff == 0:
                return row
    return -1


def find_vertical2(example: list) -> int:
    nexample = [] 
    for i in range(len(example[0])): 
        col = "" 
        for j in range(len(example)):
            col += example[j][i]
        nexample.append(col) 
    return find_mirror2(nexample)


def find_mirror(example: list) -> int:
    for row in range(1, len(example)):
        if example[row - 1] == example[row]:
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


def solve(examples: list, func1, func2):
    result = 0
    for example in examples: 
        h = func1(example)
        if not h > 0: 
            v = func2(example)
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
solve(examples, find_mirror, find_vertical)
solve(examples, find_mirror2, find_vertical2)

with open("../inputs/013.txt", "r") as fp:
    data = fp.read()

data = data.split("\n\n")
data = [d.split("\n") for d in data]
print(f"Number of examples part 1: {len(data)}")

solve(data, find_mirror, find_vertical)
solve(data, find_mirror2, find_vertical2)