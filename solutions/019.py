from collections import defaultdict


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


def create_graph(workflows: dict) -> defaultdict:
    graph = defaultdict(list) 
    for k, vals in workflows.items():
        for val in vals: 
            if ":" in val:
                graph[k].append(val.split(":")[1]) 
            else: 
                graph[k].append(val)
    return graph


# dfs until find A -> path to A -> from path build conditions/ranges for values

def create_paths(root, graph):
    paths = get_paths(root, graph)
    paths = [path.strip().split(" ") for path in paths]
    paths = [["in"] + path for path in paths if path[-1] == 'A']
    paths = [tuple(el) for el in paths]
    paths = list(set(paths))
    return paths

def get_paths(root, graph):
    paths = []
    children = graph[root]
    if children:
        for c in children:
            for el in get_paths(c, graph):
                paths.append(c + " " + el)
    else:
        paths.append("")
    return paths


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
                    # print(f"condition: {true_condition}")
                    # print(f"not conditions: {false_conditions}")
                    # there could be 0 -> n false conditions before the true condition 
                    for false_condition in false_conditions:
                        val = false_condition.split(":")[0]
                        c = val[0]
                        num = val[2:]
                        if '>' in val: 
                            # this means upper bound is smaller than num  
                            if int(num) < xmas[c][1]: 
                                xmas[c][1] = int(num) - 1
                        elif '<' in val: 
                            # lower bound 
                            if int(num) > xmas[c][0]: 
                                xmas[c][0] = int(num) + 1 
                    # there is just one true condition
                    true_condition = true_condition.split(":")[0]
                    c = true_condition[0]
                    num = true_condition[2:]
                    if '>' in true_condition: 
                        # lower bound   
                        if int(num) > xmas[c][0]: 
                            xmas[c][0] = int(num) + 1 
                    elif '<' in true_condition: 
                        # upper bound 
                        if int(num) < xmas[c][1]: 
                            xmas[c][1] = int(num) - 1

        ranges.append(xmas) 
        # print(path)
        print(xmas)

    combs = []
    for r in ranges:
        x = r['x'][1] + 1 - r['x'][0]
        m = r['m'][1] + 1 - r['m'][0]
        a = r['a'][1] + 1 - r['a'][0]
        s = r['s'][1] + 1 - r['s'][0]
        if x < 0 or m < 0 or a < 0 or s < 0:
            print(f"One path is impossible. ({x, m, a, s})") 
            # hardcoded for now because of the lnx problem
            # problem -> result is still wrong 
            combs.append(4000 * 4000 * 4000 * 677) 
            continue 
        combs.append(x * m * a * s)
    print(sum(combs))

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


workflows, ratings = parse(example)
graph = create_graph(workflows)
paths = create_paths("in", graph)

# print("Example Part 2: ", end="")
solve2(paths, workflows)

# workflows, ratings = parse(data)
# graph = create_graph(workflows)
# paths = create_paths("in", graph)

# solve2(paths, workflows)

# one open problem -> lnx has two options which overlap, in both cases you will go to A 


# source: https://github.com/jonathanpaulson/AdventOfCode/blob/master/2023/19.py
# If we started with a pile of parts with range [lo,hi], which of those parts still follow the rule op(n)?
from collections import deque

with open("../inputs/019.txt", "r") as fp: 
   data = fp.read()
rules, parts = data.split('\n\n')
R = {}
for rule in rules.split('\n'):
  name, rest = rule.split('{')
  R[name] = rest[:-1]

def new_range(op, n, lo, hi):
  if op=='>':
    lo = max(lo, n+1)
  elif op=='<':
    hi = min(hi, n-1)
  elif op=='>=':
    lo = max(lo, n)
  elif op=='<=':
    hi = min(hi, n)
  else:
    assert False
  return (lo,hi)

def new_ranges(var, op, n, xl,xh,ml,mh,al,ah,sl,sh):
  if var=='x':
    xl,xh = new_range(op, n, xl, xh)
  elif var=='m':
    ml,mh = new_range(op, n, ml, mh)
  elif var=='a':
    al,ah = new_range(op, n, al, ah)
  elif var=='s':
    sl,sh = new_range(op, n, sl, sh)
  return (xl,xh,ml,mh,al,ah,sl,sh)
# x m a s
ans = 0
Q = deque([('in', 1, 4000, 1, 4000, 1, 4000, 1,4000)])
while Q:
  state, xl,xh,ml,mh,al,ah,sl,sh = Q.pop()
  #print(state, xl, xh, ml, mh, al, ah, sl, sh, ans)
  if xl>xh or ml>mh or al>ah or sl>sh:
    continue
  if state=='A':
    print(f"ranges: {xl} {xh} / {ml} {mh} / {al} {ah} / {sl} {sh}")
    score = (xh-xl+1)*(mh-ml+1)*(ah-al+1)*(sh-sl+1)
    #print(state, xl, xh, ml, mh, al, ah, sl, sh, ans, score)
    ans += score
    continue
  elif state=='R':
    continue
  else:
    rule = R[state]
    for cmd in rule.split(','):
      applies = True
      res = cmd
      if ':' in cmd:
        cond,res = cmd.split(':')
        var = cond[0]
        op = cond[1]
        n = int(cond[2:])
        #print(state, var, op, n, *new_ranges(var, op, n, xl, xh, ml, mh, al, ah,sl, sh))
        Q.append((res, *new_ranges(var, op, n, xl, xh, ml, mh, al, ah,sl, sh)))
        xl,xh,ml,mh,al,ah,sl,sh = new_ranges(var, '<=' if op=='>' else '>=', n, xl, xh, ml, mh, al, ah,sl, sh)
        #print(xl,xh,ml,mh,al,ah,sl,sh)
      else:
        Q.append((res, xl, xh, ml, mh, al, ah, sl, sh))
        break
print(ans)