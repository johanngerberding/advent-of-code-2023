
class Node:
    def __init__(self, line: str): 
        self.name, self.left, self.right = self._parse(line)

    def _parse(self, line: str) -> tuple: 
        name = line.split("=")[0].strip()
        children = line.split("=")[1].strip().split(", ")
        children = [el.replace("(", "").replace(")", "") for el in children]  
        return (name, children[0], children[1])
    
    def __repr__(self):
        return f"{self.name}\n{self.left} | {self.right}"

def run(nodes: list, instruction: str):
    network = {} 
    for line in nodes:
        node = Node(line)
        network[node.name] = node 

    curr = network['AAA']
    assert curr.name == 'AAA'
    steps = 0 
    while True:
        for side in instruction:
            steps += 1 
            next_node = curr.left if side == 'L' else curr.right
            if next_node == 'ZZZ':
                print(f"Number of steps: {steps}") 
                return 
            curr = network[next_node]


def parse(inp: str | list) -> tuple:
    if isinstance(inp, str): 
        inp_str = inp.split("\n")
    else: 
        inp_str = inp  
    instruction = inp_str[0]
    nodes = inp_str[2:]
    return instruction, nodes


example = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

instructions, nodes = parse(example)
run(nodes, instructions)

with open("../inputs/08.txt", "r") as fp:
    inp = fp.readlines()

instructions, nodes = parse(inp)
run(nodes, instructions)
