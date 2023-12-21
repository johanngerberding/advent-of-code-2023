
example = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".split("\n")

def parse(example: list):
    example = [ex[ex.index(":") + 1:].strip().split("|") for ex in example]
    example = [[set(l.strip().split(" ")) for l in el] for el in example]

    result = 0 

    for line in example: 
        inter = line[0].intersection(line[1])
        if '' in inter:
            inter.remove('')
        if len(inter) == 1: 
            result += 1
        elif len(inter) > 0: 
            result += 2 ** (len(inter) - 1)

    print(result)

def parse2(example: list): 
    example = [ex[ex.index(":") + 1:].strip().split("|") for ex in example]
    example = [[set(l.strip().split(" ")) for l in el] for el in example]

    multiplier = {idx: 1 for idx in range(len(example))} 
    for idx, line in enumerate(example): 
        
        inter = line[0].intersection(line[1])
        if '' in inter:
            inter.remove('')

        if idx in multiplier:
            for _ in range(multiplier[idx]):
                for i in range(len(inter)):
                    if (idx + i + 1) in multiplier:
                        multiplier[idx + i + 1] += 1 
             
    print(sum(multiplier.values()))

parse(example=example)




with open("./inputs/04.txt", 'r') as fp: 
    inp = [el.strip() for el in fp.readlines()]

parse(example=inp)

parse2(example=example)
parse2(example=inp)