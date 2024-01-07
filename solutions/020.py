

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

# k -> name : value -> [type, [after], [before]]
# broadcaster : [broadcaster, [a, b, c]]

def parse(inp: str):
    example = inp.split("\n")
    G = {} 
    for el in example: 
        val = el.split("->")
        source = val[0]
        if "%" in source: 
            name = source.replace("%", "").strip() 
            t = "%" 
        elif "&" in source:
            name = source.replace("&", "").strip()
            t = "&" 
        elif "broadcaster" in source:
            name = source.strip()
            t = source.strip()
        else: 
            raise ValueError(f"There is a problem with the source value: {source}") 
        dest = val[1]
        if "," in dest: 
            dest = [el.strip() for el in dest.split(",")]
            G[name] = [t, dest]
        else: 
            G[name] = [t, [dest.strip()]] 

    print(G)

parse(example_1)
parse(example_2)