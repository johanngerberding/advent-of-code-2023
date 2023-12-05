import tqdm 


def solve(example):
    example = [el.split(":") for el in example.split("\n\n")]
    example = [[el[0], el[1].strip().split("\n")] for el in example]
    seeds = [int(el) for el in example[0][1][0].split(' ')]
    maps = example[1:]
    maps = [[el[0], [[int(num) for num in nums.split(' ')] for nums in el[1]]] for el in maps]

    # map format 
    # [map_name, [[destination range start, source range start, the range length], ... ]]

    def transform(num: int, map_info: list) -> int:  
        for info in map_info:
            if info[1] <= num < info[1] + info[2]:
                return info[0] + num - info[1] 
        return num        

    for m in maps:  
        # s2d = source2dest(map_info=m[1])
        nseed = [] 
        for seed in seeds:
            nseed.append(transform(seed, m[1]))
        seeds = nseed

    print(min(seeds))


example = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

with open("../inputs/05.txt", 'r') as fp: 
    inp = fp.read()


solve(example=example)
solve(example=inp)
