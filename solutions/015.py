
class Lens:
    def __init__(self, inp: str):
        self.label, self.focal_length, self.hash  = self._parse(inp) 

    def _parse(self, inp: str) -> tuple:
        if "=" in inp:
            info = inp.split("=")
            assert len(info) == 2
            h = hash(info[0]) 
            return info[0], int(info[1]), h
        elif "-" in inp:
            info = inp.split("-") 
            h = hash(info[0])
            return info[0], 0, h
        else:
            raise ValueError("No = or - in string")

    def __eq__(self, other):
        if self.label == other.label:
            return True 
        return False



def hash(word: str) -> int: 
    val = 0 
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
        res += hash(el)
    print(res)

def solve2(inp: str):
    elements = inp.replace("\n", "").split(",")
    boxes = {i: [] for i in range(256)}
    
    for el in elements: 
        lens = Lens(el)
        if "=" in el: 
            if lens in boxes[lens.hash]:
                # replace lens
                idx = boxes[lens.hash].index(lens) 
                boxes[lens.hash][idx] = lens 
            else: 
                # add lens
                boxes[lens.hash].append(lens)
        elif "-" in el: 
            # remove lens
            if lens in boxes[lens.hash]:
                boxes[lens.hash].remove(lens)
        else: 
            raise ValueError("Missing - or =")
    
    focusing_power = 0 
    for box, lenses in boxes.items(): 
        for slot, lens in enumerate(lenses): 
            focusing_power += (box + 1) * (slot + 1) * lens.focal_length

    print(focusing_power)

example = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""
print("Example: ", end="")
solve(example)
print("Example for part 2: ", end="")
solve2(example)

with open("../inputs/015.txt", "r") as fp: 
    data = fp.read()

print("Part 1: ", end="")
solve(data)
print("Part 2: ", end="")
solve2(data)
