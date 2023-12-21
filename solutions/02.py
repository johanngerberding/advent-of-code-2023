
R = 12 
G = 13
B = 14

def parse1(lines: list): 
    # id , rbg per game
    sm = 0  
    for line in lines: 
        idx = int(line[:line.index(":")].split(' ')[-1])
        line = line[line.index(":") + 1:] 
        games = line.split(";")
        games = [game.strip().split(",") for game in games] 
        possible = True  
        for game in games: 
            valid = True  
            for el in game: 
                sc = el.strip().split(' ')
                score = int(sc[0]) 
                color = sc[1]
                if color == "red" and score > R: 
                    valid = False 
                if color == "blue" and score > B: 
                    valid = False 
                if color == "green" and score > G: 
                    valid = False 

            if not valid: 
                possible = False 
                break  
        if possible:
            sm += idx 

    return sm 
        
def parse2(lines: list): 
    # id , rbg per game
    sm = 0  
    for line in lines: 
        r, g, b = 0, 0, 0 
        # idx = int(line[:line.index(":")].split(' ')[-1])
        line = line[line.index(":") + 1:] 
        games = line.split(";")
        games = [game.strip().split(",") for game in games] 
        for game in games: 
            for el in game: 
                sc = el.strip().split(' ')
                score = int(sc[0]) 
                color = sc[1]
                if color == "red" and score > r: 
                    r = score  
                if color == "blue" and score > b: 
                    b = score 
                if color == "green" and score > g: 
                    g = score  
        
        power = r * g * b 
        sm += power 

    return sm 
 

example = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

example = example.split("\n")

sum_ids = parse1(example)
print(f"Example 1: {sum_ids}")

with open("./inputs/02.txt", 'r') as fp:
    input1 = [el.strip() for el in fp.readlines()]

sum_ids1 = parse1(input1)
print(f"Part 1: {sum_ids1}")

sum_powers2 = parse2(example)
print(f"Example 2: {sum_powers2}")

sum_powers2 = parse2(input1)
print(f"Part 2: {sum_powers2}")
