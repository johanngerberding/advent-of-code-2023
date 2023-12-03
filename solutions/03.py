
def is_symbol(c: str) -> bool: 
    if not c.isdigit() and c != '.':
        return True 
    return False 

def get_surrounding(x: int, y: int, max_x: int, max_y: int) -> list: 
    coords = [
        (x-1, y),
        (x-1, y-1),
        (x-1, y+1),
        (x, y-1),
        (x, y+1),
        (x+1, y),
        (x+1, y-1),
        (x+1, y+1),
    ]
    return [
        pos for pos in coords if pos[0] >= 0 and pos[0] <= max_x and pos[1] >= 0 and pos[1] <= max_y
    ]

def get_num_surrounding(pos: list, max_x: int, max_y: int) -> list: 
    surrs = [] 
    for p in pos: 
        surrs += get_surrounding(p[0], p[1], max_x, max_y)
    
    for p in pos:
        if p in surrs: 
            surrs.remove((p[0], p[1]))
    return list(set(surrs))

def check_engine(example: list):
    numbers = [] 
    symbols = [] 

    max_x = len(example[0]) - 1  
    max_y = len(example) - 1 

    for row, ex in enumerate(example):
        # first all symbols 
        for col, c in enumerate(ex):  
            if not c.isdigit() and c != '.':
                symbols.append((row, col))

        # replace symbols 
        ex_list = list(ex)
        for pos in symbols:
            if pos[0] == row:
                ex_list[pos[1]] = "."
        ex = ''.join(ex_list)
        # then get numbers  
        nums = [el for el in ex.split(".") if el != '']
        idxs = [ex.index(num) for num in nums]

        for num, idx in zip(nums, idxs): 
            numbers.append((int(num), [(row, idx + col) for col in range(len(num))]))

    result = 0
    correct_numbers = []
    for number in numbers: 
        num, pos = number
        surrounding = get_num_surrounding(pos, max_x, max_y) 
        for sym in symbols: 
            if sym in surrounding:
                correct_numbers.append(num) 
                result += num 
                continue

    print(result)
    print(correct_numbers)
    print(sum(correct_numbers))

example = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

example = example.split("\n")

check_engine(example)

with open("./inputs/03.txt", 'r') as fp: 
    inp = [el.strip() for el in fp.readlines()]

check_engine(inp)