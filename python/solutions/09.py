
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
        lasts = [] 
        lasts.append(line[-1])
        curr = line.copy() 
        while not check_zero(curr):
            curr = get_diffs(curr)
            if len(curr) > 0: 
                lasts.append(curr[-1])
        result += sum(lasts) 

    print(f"Result: {result}")


example = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""
run(example)

with open("../inputs/09.txt", 'r') as fp:
    data = fp.read()

run(data)