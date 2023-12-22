from itertools import product
import time 


def timer(func): 
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        val = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        if elapsed > 1.: 
            print(f"{func.__name__} took {elapsed:.2f}s")
        return val 
    return wrapper 

@timer
def valid(line: str, parts: list) -> bool:
    elements = [el for el in line.split(".") if el != '']
    if len(elements) != len(parts):
        return False
    for i, element in enumerate(elements): 
        if not len(element) == parts[i]:
            return False
    return True

# this is the problem, its too complex and inefficient 
@timer
def get_combinations(line: str, parts: list) -> tuple:
    idxs = [i for i, el in enumerate(line) if el == '?']
    return list(product('.#', repeat=len(idxs))), idxs 


@timer
def extend(inp: str) -> list:
    example = inp.split("\n")
    example = [row.split(" ") for row in example]
    example = [[el[0], [int(num) for num in el[1].split(",")]] for el in example]

    extended = []
    for el in example: 
        spring, groups = el[0], el[1]
        extended_spring, extended_groups = spring, groups.copy() 
        for _ in range(4): 
            extended_spring += f"?{spring}"
            extended_groups.extend(groups)
        extended.append([extended_spring, extended_groups])

    return extended


def solve(inp: str, part1=True):
    if part1: 
        example = inp.split("\n")
        example = [row.split(" ") for row in example]
        example = [[el[0], [int(num) for num in el[1].split(",")]] for el in example]
    else: 
        example = extend(inp) 
    result = 0 
    for i, line in enumerate(example):
        print(f"Lets get all the combinations of line {i}")
        combinations, idxs = get_combinations(line[0], line[1])
        valid_combinations = 0 
        print(f"Now let's check all the combinations")
        for combination in combinations: 
            nline = list(line[0])
            for idx, el in zip(idxs, combination): 
                nline[idx] = el
            if valid(''.join(nline), line[1]): 
                valid_combinations += 1

        result += valid_combinations

    return result

# brute force?? 
# try all possible combinations and check if valid?? 
example = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""


# example_res = solve(example)
# print(f"Example result: {example_res}")

# with open("../inputs/012.txt", 'r') as fp: 
#     data = fp.read()

# part1 = solve(data)
# print(f"Part 1: {part1}")

part2 = solve(example, part1=False)
print(f"Part 2 example: {part2}")

# brute force works for the first part but not for the second
# use dynamic programming to solve the second part?? 