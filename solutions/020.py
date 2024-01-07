

# flip-flop module = % , is either on or off
# high pulse ignored, low pulse flips on <-> off 

# conjuction modules = & 
# remember last pulse, from each of their connected modules

# broadcast module -> sends the same pulse to all modules 
# button module -> low pulse to broadcaster 

class Module:
    def __init__(self, name: str, val: str, adjs: list):
        self.name = name 
        self.val = val
        self.adjs = adjs

example_1 = """broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a"""

example_2 = """broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output"""

# k -> name : value -> [state, type, [after], [before]]
# broadcaster : [broadcaster, [a, b, c]]
# after I am through, go to all conjunction modules and add before modules?? 

def parse(inp: str):
    example = inp.split("\n")
    G = {} 
    for el in example: 
        val = el.split("->")
        source = val[0]
        if "%" in source: 
            name = source.replace("%", "").strip() 
            t = "%" 
            state = 0  # off
            before = None
        elif "&" in source:
            name = source.replace("&", "").strip()
            t = "&" 
            state = None
            before = []
        elif "broadcaster" in source:
            name = source.strip()
            t = source.strip()
            state = None
            before = None
        else: 
            raise ValueError(f"There is a problem with the source value: {source}") 
        dest = val[1]
        if "," in dest: 
            dest = [el.strip() for el in dest.split(",")]
            G[name] = [state, t, dest, before]
        else: 
            G[name] = [state, t, [dest.strip()], before] 

    # fill in before lists  
    cons = [] 
    for k, v in G.items(): 
        if v[1] == "&":
            cons.append(k)

    for con in cons: 
        for k, v in G.items():
            if con in v[2]:
                G[con][3].append(k)

    print(G)
    return G

G = parse(example_1)

Q = ["broadcaster"]

while Q: 
    curr = Q.pop(0)
    module = G[curr]
    # broadcaster -> send low pulse to all connections 

    for nxt in module[2]: 
        ...
        # do stuff 
        # check all &conjunction modules 
        # send from conjuction modules
        

G = parse(example_2)