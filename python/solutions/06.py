example = """Time:      7  15   30
Distance:  9  40  200"""

with open("../inputs/06.txt", 'r') as fp:
    inp = fp.read()


def parse(inp: str) -> list:
    inp = [el.split(":")[1].strip().split(' ') for el in inp.split("\n")]
    inp = [[int(num) for num in el if num != ''] for el in inp]
    pairs = list(zip(inp[0], inp[1]))
    return pairs 

def solve(pairs: list):
    multi = 1 
    for pair in pairs:
        chances = 0 
        for i in range(pair[0]):
            speed = i 
            steps = pair[0] - i 
            res = speed * steps  
            if res > pair[1]:
                # print(f"Broke record: {res}")
                chances += 1

        multi *= chances
    print(multi)

example = parse(example)
solve(example)

part1 = parse(inp)
solve(part1)
