
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
            print(f"Found two same rows: {row}") 
            up = ''.join(example[:row - 1][::-1])
            down = ''.join(example[row + 1:])
            if len(up) > len(down):
                up = up[:len(down)]
            else: 
                down = down[:len(up)] 
            print(f"up: {up}")
            print(f"down: {down}")
            diff = count_diff_symbols(up, down) 
            print(f"Number of different symbols: {diff}") 
            if diff == 1:
                return row
        if diff == 1: 
            print(f"Found two nearly the same rows: {row}") 
            up = ''.join(example[:row - 1][::-1])
            down = ''.join(example[row + 1:])
            if len(up) > len(down):
                up = up[:len(down)]
            else: 
                down = down[:len(up)] 
            print(f"up: {up}")
            print(f"down: {down}")
            diff = count_diff_symbols(up, down) 
            print(f"Number of different symbols: {diff}") 
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


def solve2(examples: list):
    result = 0
    for example in examples: 
        h = find_mirror2(example)
        if not h > 0: 
            v = find_vertical2(example)
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
solve2(examples)

with open("../inputs/013.txt", "r") as fp:
    data = fp.read()

data = data.split("\n\n")
data = [d.split("\n") for d in data]
print(f"Number of examples part 1: {len(data)}")

solve(data)
solve2(data)