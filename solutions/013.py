

example = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""

examples = example.split("\n\n")
examples = [example.split("\n") for example in examples]
print(f"Number of examples: {len(examples)}")


# another idea 
# left and right stack
# up and down 


for i, example in enumerate(examples): 
     
    ...



line_length = len(examples[0][0])
examples = ["".join(example) for example in examples]
print(examples)
# find the reflection line 
for example in examples:
    for i in range(1, len(example)):
        left = example[:i]
        right = example[i:][::-1] # reverse it 
        if len(left) > len(right): 
            if left.startswith(right): 
                print(f"Found mirror at pos: {i % line_length}")
        else: 
            if right.startswith(left): 
                print(f"Found mirror at pos: {i % line_length}")



