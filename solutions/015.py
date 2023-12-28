def hash(word: str, val: int) -> int: 
    for c in word: 
        asc = ord(c) 
        val += asc 
        val *= 17 
        rem = val % 256 
        val = rem 

    return val 

def solve(inp: str):
    elements = inp.replace("\n", "").split(",")
    res = 0 
    for el in elements: 
        res += hash(el, 0)
    print(res)

example = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""
print("Example: ", end="")
solve(example)

with open("../inputs/015.txt", "r") as fp: 
    data = fp.read()

print("Part 1: ", end="")
solve(data)
