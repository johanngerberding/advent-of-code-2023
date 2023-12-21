
def check_zero(line: list):
    for el in line: 
        if el != 0:
            return False
    return True


def get_diffs(line: list) -> list:
    return [line[i+1] - line[i] for i in range(len(line) - 1)] 

def run(inp: str):
    lines = inp.split("\n")
    lines = [[int(el) for el in li.split(" ")] for li in lines]
    result = 0
    for line in lines:
        lasts = 0 
        lasts += line[-1]
        curr = line.copy() 
        while not check_zero(curr):
            curr = get_diffs(curr)
            if len(curr) > 0: 
                lasts += curr[-1]
        result += lasts 

    print(f"Result: {result}")

def run2(inp: str):
    lines = inp.split("\n")
    lines = [[int(el) for el in li.split(" ")] for li in lines]
    result = 0
    for line in lines:
        firsts = [] 
        firsts.append(line[0])
        curr = line.copy() 
        while not check_zero(curr):
            curr = get_diffs(curr)
            if len(curr) > 0: 
                firsts.append(curr[0])
        firsts = list(reversed(firsts))
        sub = 0  
        for i in range(1, len(firsts)):
            sub = firsts[i] - sub 
        result += sub  
    print(f"Result: {result}")



example = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""
run(example)

run2(example)

with open("../inputs/09.txt", 'r') as fp:
    data = fp.read()

run(data)
run2(data)