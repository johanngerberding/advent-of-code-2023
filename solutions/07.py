from collections import Counter 

STRENGTHS = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
STRENGTHS_2 = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


class Hand:
    def __init__(self, line: str, part2: bool = False):  
        self.hand, self.bid = self._parse(line)  
        self.part2 = part2
        self.type = self._type() 

    def __str__(self): 
        return self.hand 
    
    def __repr__(self) -> str:
        return self.hand + f" ({self.type})"

    def _parse(self, line: str) -> tuple:
        line_ = line.strip().split(" ")
        assert len(line_) == 2     
        return (line_[0], int(line_[1])) 

    def __lt__(self, other): 
        # if same types, compare in detail 
        if self.type == other.type:
            for i in range(len(self.hand)):             
                if self.hand[i] != other.hand[i]:
                    strengths = STRENGTHS if not self.part2 else STRENGTHS_2 
                    shand = strengths.index(self.hand[i])
                    sother = strengths.index(other.hand[i]) 
                    # the smaller index wins  
                    return shand > sother 
        
        # if different types, return higher type 
        return self.type > other.type

    def _type(self): 
        # determine which kind of hand this is 
        c = Counter(self.hand)
        _type = None
        if len(c.keys()) == 1: 
            # five of a kind  
            _type = 0  
        elif len(c.keys()) == 5: 
            # high card 
            _type = 6  
        elif len(c.keys()) == 2: 
            if sorted(list(c.values()))[0] == 1:
                # four of a kind 
                _type = 1 
            else: 
                # full house  
                _type = 2               
        elif len(c.keys()) == 3:
            # determine if two pairs or three of a kind 
            if sorted(list(c.values()))[-1] == 3:
                # three of a kind 
                _type = 3 
            else: 
                # two pairs 
                _type = 4
        # one pair 
        else: 
            _type = 5 
        if not self.part2: 
            return _type 

        if "J" in self.hand: 
            jokers = c['J']
            if jokers >= 4:
                return 0 
            if jokers == 3:
                del c['J'] 
                if 2 in c.values():
                    return 0 
                return 1 
            if jokers == 2:
                del c["J"] 
                if 3 in c.values():
                    return 0 
                if 2 in c.values():
                    return 1
                return 3 
            if jokers == 1:
                del c["J"]
                if 4 in c.values():
                    return 0 
                if 3 in c.values():
                    return 1 
                if 2 in c.values():
                    if 1 in c.values():
                        return 3  
                    return 2
                return 5 
        else: 
            return _type
    

example = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""


def solve(inp: str, part2: bool=False):
    hands = []
    for line in inp.split("\n"): 
        hands.append(Hand(line, part2))
    # print(hands) 
    hands.sort()
    # print(f"sorted: {hands}")
    result = 0 
    for idx, hand in enumerate(hands): 
        rank = idx + 1 
        result += (rank * hand.bid)
    print(result)

print("Part 1")
print("Example: ", end="")
solve(example)

with open("../inputs/07.txt", "r") as fp: 
    inp = fp.read()
print("Input: ", end="")
solve(inp)
print()
print("Part 2")
print("Example: ", end="")
solve(example, True)
print("Input: ", end="")
solve(inp, True)