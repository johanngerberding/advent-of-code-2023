


def parse(inp: str): 
    example = inp.split("\n\n")
    workflow = example[0].split("\n")
    ratings_inp = [el[1:-1].split(",") for el in example[1].split("\n")]

    ratings = []
    for rating in ratings_inp: 
        parsed = {}
        for el in rating:
            kv = el.split("=")
            parsed[kv[0]] = int(kv[1])
        ratings.append(parsed)

    workflows = {}
    for wf in workflow: 
        s = wf.index("{")
        name = wf[:s]
        rules = wf[s + 1:-1].split(",")
        assert len(rules) > 1 
        workflows[name] = rules
    return workflows, ratings


def process(curr: list, rating: dict) -> str:
    workflow = curr.copy() 
    while len(workflow) > 1: 
        condition = workflow.pop(0)
        condition = condition.split(":") 
        assert len(condition) == 2 
        nxt = condition[1] 
        if ">" in condition[0]:
            cond_parts = condition[0].split(">")
            symbol = cond_parts[0]
            value = int(cond_parts[1])
            if rating[symbol] > value: 
                return nxt 
        elif "<" in condition[0]:
            cond_parts = condition[0].split("<")
            symbol = cond_parts[0]
            value = int(cond_parts[1])
            if rating[symbol] < value: 
                return nxt
        else: 
            print("Problem") 
    return workflow[0] 

def solve(inp) -> int:
    workflows, ratings = parse(inp)
    result = 0
    for rating in ratings: 
        curr = workflows['in']
        while True: 
            nxt = process(curr, rating)
            if nxt == 'R':
                break 
            if nxt == 'A':
                result += sum([v for v in rating.values()])
                break
            curr = workflows[nxt] 

    return result


example = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""

print(f"Example result: {solve(example)}")

with open("../inputs/019.txt", "r") as fp: 
    data = fp.read()

print(f"Part 1: {solve(data)}")


# part 2 -> (x, m, a, s) 
# all possible combinations from 1 to 4000 for every value 
# how many will be accepted
# how to do this efficiently??? 
# other way around, get all combinations that lead to 'A' as ranges? 
# build a graph from the workflow 
# find all nodes with an 'A' as a possible outcome 
# backtrack from 'A'?? 
# output ->  a: [condition for every reachable 'A'?] 


workflows, ratings = parse(example)
print(workflows)
from collections import defaultdict

graph = defaultdict(list) 
for k, vals in workflows.items():
    for val in vals: 
        if ":" in val:
            cond = val.split(":")[0] 
            graph[k].append(val.split(":")[1]) 
        else: 
            graph[k].append(val)

print(graph)


# dfs until find A -> path to A -> from path build conditions/ranges for values

def get_paths(root):
    x = []
    children = graph[root]
    if children:
        for c in children:
            for el in get_paths(c):
                x.append(c + " " + el)
    else:
        x.append("")
    return x


def solve2(paths: list, workflows: dict):
    ranges = [] 
    for path in paths:
        xmas = {
            'x': [1, 4000],
            'm': [1, 4000],
            'a': [1, 4000],
            's': [1, 4000],
        }
        for i in range(1, len(path)):
            curr = path[i -1]
            if curr == 'A':
                break
            nxt = path[i]
            workflow = workflows[curr]
            true_condition = None 
            for i, option in enumerate(workflow): 
                if nxt in option: 
                    true_condition = option 
                    false_conditions = workflow[:i]
                    print(f"condition: {true_condition}")
                    print(f"not conditions: {false_conditions}")
                    
                    for false_condition in false_conditions:
                        val = false_condition.split(":")[0]
                        c = val[0]
                        num = val[2:]
                        if '>' in val: 
                            # this means upper bound is smaller than num  
                            if int(num) < xmas[c][1]: 
                                xmas[c][1] = int(num) 
                        elif '<' in val: 
                            # lower bound 
                            if int(num) > xmas[c][0]: 
                                xmas[c][0] = int(num)

                    true_condition = true_condition.split(":")[0]
                    c = true_condition[0]
                    num = true_condition[2:]
                    if '>' in true_condition: 
                        # lower bound   
                        if int(num) > xmas[c][0]: 
                            xmas[c][0] = int(num) 
                    elif '<' in true_condition: 
                        # upper bound 
                        if int(num) < xmas[c][1]: 
                            xmas[c][1] = int(num)
    
        ranges.append(xmas) 

    for r in ranges:
        x =  list(range(r['x'][0], r['x'][1] + 1))
        m =  list(range(r['m'][0], r['m'][1] + 1))
        a =  list(range(r['a'][0], r['a'][1] + 1))
        s =  list(range(r['s'][0], r['s'][1] + 1))
        unique_combinations = set() 
        for i in range(len(x)):
            for j in range(len(m)):
                for p in range(len(a)):
                    for k in range(len(s)):
                       unique_combinations.add((x[i], m[j], a[p], s[k])) 

        print(len(unique_combinations))

paths = get_paths("in")
paths = [path.strip().split(" ") for path in paths]
paths = [["in"] + path for path in paths if path[-1] == 'A']
print(paths)

solve2(paths, workflows)
