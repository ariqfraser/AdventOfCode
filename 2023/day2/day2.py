import re
from functools import reduce
import operator

raw = open('./part1.txt', 'r').read().split("\n")
validGames = []
for i,line in enumerate(raw):
    pulls = {'r': 0, 'g': 0, 'b': 0}
    for quantity, colour in re.findall(r'(\d+)\s(\w)', line):
        pulls[colour] = max(int(quantity), pulls[colour])
    validGames.append(i+1 if pulls['r'] <= 12 and pulls['g'] <= 13 and pulls['b'] <=14 else 0)
print('Part1: {}'.format(sum(validGames)))

# -------------------- PART 2 ------------------

def power(iterable):
    return reduce(operator.mul, iterable, 1)

gamePowers = []
for i,line in enumerate(raw):
    pulls = {'r': 0, 'g': 0, 'b': 0}
    for quantity, colour in re.findall(r'(\d+)\s(\w)', line):
        pulls[colour] = max(int(quantity), pulls[colour])
    gamePowers.append(power(pulls.values()))
print('Part2: {}'.format(sum(gamePowers)))