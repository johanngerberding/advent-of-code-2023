from collections import Counter 

STRENGTHS = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

class Hand:
    def __init__(self, line: str,):
        self.hand, self.bid = self._parse(line)         
        self.type = self._type() 

    def __str__(self): 
        return self.hand 
    
    def __repr__(self) -> str:
        return self.hand

    def _parse(self, line: str) -> tuple:
        line_ = line.strip().split(" ")
        assert len(line_) == 2     
        return (line_[0], int(line_[1])) 

    def __lt__(self, other): 
        # if same types, compare in detail 
        if self.type == other.type:
            for i in range(len(self.hand)):             
                if self.hand[i] != other.hand[i]: 
                    shand = STRENGTHS.index(self.hand[i])
                    sother = STRENGTHS.index(other.hand[i]) 
                    # the smaller index wins  
                    return shand > sother 
        
        # if different types, return higher type 
        return self.type > other.type

    def _type(self): 
        # determine which kind of hand this is 
        c = Counter(self.hand)
        if len(c.keys()) == 1: 
            # five of a kind  
            return 0 
        if len(c.keys()) == 5: 
            # high card 
            return 6
        if len(c.keys()) == 2: 
            if sorted(list(c.values()))[0] == 1:
                # four of a kind 
                return 1 
            else: 
                # full house  
                return 2               
        if len(c.keys()) == 3:
            # determine if two pairs or three of a kind 
            if sorted(list(c.values()))[-1] == 3:
                # three of a kind 
                return 3 
            else: 
                # two pairs 
                return 4
        # one pair 
        return 5 
    

example = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""


def solve(inp: str):
    hands = []
    for line in inp.split("\n"): 
        hands.append(Hand(line))
    hands.sort()
    result = 0 
    for idx, hand in enumerate(hands): 
        rank = idx + 1 
        result += (rank * hand.bid)
    print(result)

solve(example)

with open("../inputs/07.txt", "r") as fp: 
    inp = fp.read()

solve(inp)