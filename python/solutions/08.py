
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
    while not curr.name == 'ZZZ':
        inst =  instruction[steps % len(instruction)]
        assert inst in ['L', 'R']
        next_node = curr.left if inst == 'L' else curr.right
        steps += 1 
        curr = network[next_node]
    print(f"Number of steps: {steps}") 
 
def run2(nodes: list, instruction: str):
    network = {} 
    for line in nodes:
        node = Node(line)
        network[node.name] = node 

    curr = [node for name, node in network.items() if name[-1] == 'A']
    print(f"Number of starting nodes: {len(curr)}") 
    steps = 0 
    while not end(curr):
        inst =  instruction[steps % len(instruction)]
        assert inst in ['L', 'R']
        curr = [network[node.left] if inst == 'L' else network[node.right] for node in curr]
        steps += 1 
        # if steps % 100000 == 0: 
            # print(f"steps: {steps}")
    print(f"Number of steps: {steps}") 

def end(nodes: list) -> bool:
    for node in nodes: 
        if node.name[-1] != 'Z':
            return False 
    return True 

def parse(inp: str | list) -> tuple:
    if isinstance(inp, str): 
        inp_str = inp.split("\n")
    else: 
        inp_str = inp  
    instruction = inp_str[0].strip()
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

example = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

instructions, nodes = parse(example)
run(nodes, instructions)

with open("../inputs/08.txt", "r") as fp:
    inp = fp.readlines()

instructions, nodes = parse(inp)
run(nodes, instructions)

run2(nodes, instructions)

example2 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

# instructions, nodes = parse(example2)
# run2(nodes, instructions)

