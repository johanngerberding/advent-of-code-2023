from itertools import combinations_with_replacement, permutations, product


def valid(line: str, parts: list) -> bool:
    elements = [el for el in line.split(".") if el != '']
    if len(elements) != len(parts):
        return False
    for i, element in enumerate(elements): 
        if not len(element) == parts[i]:
            return False
    return True

def get_combinations(line: str) -> tuple:
    idxs = [i for i, el in enumerate(line) if el == '?']
    return list(product('.#', repeat=len(idxs))), idxs 


def solve(inp: str):
    example = inp.split("\n")
    example = [row.split(" ") for row in example]
    example = [[el[0], [int(num) for num in el[1].split(",")]] for el in example]
    result = 0 
    for line in example:
        combinations, idxs = get_combinations(line[0])
        valid_combinations = 0 
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

example_res = solve(example)
print(f"Example result: {example_res}")

with open("../inputs/012.txt", 'r') as fp: 
    data = fp.read()

part1 = solve(data)
print(f"Part 1: {part1}")
