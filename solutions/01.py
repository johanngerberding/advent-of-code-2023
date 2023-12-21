

substrings = ["one", "two", "three", "four", "five", "six", "seven", "eight",
              "nine"] 

example_1 = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

example_1 = example_1.split("\n")

example_2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

example_2 = example_2.split("\n")

def get_num_1(line: str):
    for i, c in enumerate(line): 
        if c.isdigit():  
            return c 
        else: 
            for j, substr in enumerate(substrings): 
                if line[i:].startswith(substr):
                    return str(j + 1)


def get_num_2(line: str):
    for i in range(len(line) - 1, -1, -1):
        if line[i].isdigit():
            return line[i]
        else: 
            for j, substr in enumerate(substrings):
                if line[:i + 1].endswith(substr):
                    return str(j + 1)


def get_calib(lines: list) -> int: 
    sm = 0 
    for i, line in enumerate(lines): 
        num1 = get_num_1(line)
        num2 = get_num_2(line)
        sm += int(num1 + num2) 

    return sm 

with open("../inputs/01.txt") as f:
    inp = [el.strip() for el in f.readlines()] 


# print(f"example part 1: {get_calib(example_1)}")
# print(f"part 1: {get_calib(inp)}")

print(f"example part 2: {get_calib(example_2)}")
print(f"part 2: {get_calib(inp)}")

