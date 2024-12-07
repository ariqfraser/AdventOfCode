from os import path
def combinePos(pos1, pos2):
    return (pos1[0] + pos2[0], pos1[1] + pos2[1])

N = (0, -1)
E = (1, 0)
S = (0, 1)
W = (-1, 0)
NE = combinePos(N, E)
NW = combinePos(N, W)
SE = combinePos(S, E)
SW = combinePos(S, W)

def getCharMatrix(filename: str):
    file = open(path.join(path.dirname(path.abspath(__file__)), filename), 'r')
    return [list(line.replace('\n', '').lower()) for line in file.readlines()]

def linearTraverse(matrix, startingPos, offset, toFind) -> bool:
    startingX, startingY = startingPos
    offsetX, offsetY = offset
    foundChar = matrix[startingY][startingX]
    if foundChar == toFind[0:1]:
        # at end of toFind string
        if len(toFind) == 1:
            # print(f"Found xmas, toFind {toFind}")
            return True

        nextX = startingX + offsetX
        nextY = startingY + offsetY
        # out of bounds
        if nextX == len(matrix[0]) or nextY == len(matrix) or nextX < 0 or nextY < 0:
            return False
        return linearTraverse(matrix, (nextX, nextY), offset, toFind=toFind[1:])
    return False

def part1():
    charMatrix = getCharMatrix('part1.txt')
    foundCount = 0
    for y in range(len(charMatrix)):
        for x in range(len(charMatrix[0])):
            if charMatrix[y][x] == 'x':
                startingPos = (x, y)
                foundCount += 1 if linearTraverse(charMatrix, startingPos, E, toFind='xmas') else 0
                foundCount += 1 if linearTraverse(charMatrix, startingPos, W, toFind='xmas') else 0
                foundCount += 1 if linearTraverse(charMatrix, startingPos, N, toFind='xmas') else 0
                foundCount += 1 if linearTraverse(charMatrix, startingPos, S, toFind='xmas') else 0

                foundCount += 1 if linearTraverse(charMatrix, startingPos, SE, toFind='xmas') else 0 
                foundCount += 1 if linearTraverse(charMatrix, startingPos, NE, toFind='xmas') else 0
                foundCount += 1 if linearTraverse(charMatrix, startingPos, SW, toFind='xmas') else 0
                foundCount += 1 if linearTraverse(charMatrix, startingPos, NW, toFind='xmas') else 0
    print(f'Found XMAS {foundCount} times')

def checkCrossMAS(matrix, startingPos):
    directionsToCheck = [NE, NW, SE, SW]
    foundM, foundS = [], []
    for offset in directionsToCheck:
        foundM.append(linearTraverse(matrix, startingPos, offset, toFind='am'))
        foundS.append(linearTraverse(matrix, startingPos, offset, toFind='as'))
    if foundM.count(True) == 2 and foundS.count(True) == 2: 
        print(startingPos, foundM, foundS)
    return foundM.count(True) == 2 and foundS.count(True) == 2

def part2():
    charMatrix = getCharMatrix('sample.txt')
    foundCount = 0
    for y in range(len(charMatrix)):
        for x in range(len(charMatrix[0])):
            if charMatrix[y][x] == 'a':
               foundCount += 1 if checkCrossMAS(charMatrix, (x, y)) else 0
                 
    print(f'Found X-MAS (cross) {foundCount} times')

part1()
part2()