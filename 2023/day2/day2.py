import re
from math import isnan

# raw = open("./part1.txt", "r").read()
# lines = raw.split("\n")
# validGames = [];

# for gameIndex, line in enumerate(lines):
#     formatted = re.findall(r'(\d+|\b\w+\b)', line)
#     formatted = formatted[2:]
#     cubes = {
#         'red': 0,
#         'blue': 0,
#         'green': 0
#     }
#     for i, v in enumerate(formatted):
#         if v.isnumeric():
#             cubes[formatted[i+1]] += int(v)
#         else:
#             continue
#     # print(cubes,gameIndex + 1)
#     if cubes['red'] <= 12 and cubes['green'] <= 13 and cubes['blue'] <= 14:
#         validGames.append(gameIndex + 1)
# print(validGames)
# print(sum(int(i) for i in validGames))

raw = open("./part1.txt", "r").read().split("\n")
validGames = []
for line in raw:
    gameNumber = int(re.findall(r'Game\s(\d+):', line)[0])
    red = sum(int(v) for v in re.findall(r'(\d)\sred', line))
    green = sum(int(v) for v in re.findall(r'(\d)\sgreen', line))
    blue = sum(int(v) for v in re.findall(r'(\d)\sblue', line))

    print('{}: Red {} Green {} Blue {}'.format(gameNumber, red, green, blue))

    if red <= 12 and green <= 13 and blue <=14:
        validGames.append(gameNumber)

print(validGames)
print(sum(validGames))

# ! 489