from itertools import combinations_with_replacement, permutations, product


def valid(line: str, parts: list):
    ...


def get_combinations(line: str) -> list:
    num_elements = len([el for el in line if el == '?'])
    print(num_elements) 
    return list(product('.#', repeat=num_elements))


example = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""


example = example.split("\n")
example = [row.split(" ") for row in example]
example = [[el[0], [int(num) for num in el[1].split(",")]] for el in example]
print(example)
combinations = get_combinations(example[0][0])
print(combinations)
# brute force?? 
# try all possible combinations and check if valid?? 

