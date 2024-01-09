

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

class Module:
    def __init__(self, name, kind, state, adjs, before):
        self.name = name 
        self.kind = kind 
        self.state = state
        self.adjs = adjs 
        self.before = before 

    def __repr__(self): 
        return f"{self.name} | {self.kind} | {self.state} | {self.adjs} | {self.before}"
    

    def process(self, pulse: int) -> dict: 
        # receives a low pulse {0} or a high pulse {1}
        # flip-flop 
        instructions = {} 
        if pulse == 1:
            # high pulse -> do nothing 
            return instructions 
        elif pulse == 0: 
            if self.state == 0: 
                # send high pulse adjs 
                for adj in self.adjs: 
                    instructions[adj] = 1
            else: 
                # send low pulse to adjs 
                for adj in self.adjs: 
                    instructions[adj] = 0 

        return instructions


def parse(inp: str):
    example = inp.split("\n")
    G = {} 
    for el in example: 
        val = el.split("->")
        source = val[0]
        if "%" in source: 
            module = Module(
                name=source.replace("%", "").strip(),
                kind="%",
                state=0,
                adjs=None,
                before=None,
            ) 
        elif "&" in source:
            module = Module(
                name=source.replace("&", "").strip(),
                kind="&",
                state=0,
                adjs=None,
                before=[],
            ) 
        elif "broadcaster" in source:
            module = Module(
                name=source.strip(),
                kind=source.strip(),
                state=None,
                adjs=None,
                before=None,
            ) 
        else: 
            raise ValueError(f"There is a problem with the source value: {source}") 
        
        dest = val[1]
        if "," in dest: 
            dest = [el.strip() for el in dest.split(",")]
            module.adjs = dest 
            G[module.name] = module 
        else: 
            module.adjs = [dest.strip()]
            G[module.name] = module 

    # fill in before lists  
    cons = [] 
    for k, v in G.items(): 
        if v.kind == "&":
            cons.append(k)

    for con in cons: 
        for k, v in G.items():
            if con in v.adjs:
                G[con].before.append(k)

    return G

G = parse(example_1)

for k, v in G.items():
    print(v)

Q = ["broadcaster"]
instructions = {}

while Q: 
    curr_name = Q.pop(0)
    module = G[curr_name]
    
    # broadcaster -> send low pulse to all connections 
    
    for nxt in module.adjs: 
        if curr_name == "broadcaster": 
            # low pulse 
            next_instructions = nxt.process(0) 
            # now check conjunction modules (&) 
            # send from conjuction modules
          

G = parse(example_2)