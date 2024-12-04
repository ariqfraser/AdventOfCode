from os import path

file = open(path.join(path.dirname(path.abspath(__file__)), 'part1.txt'), 'r')
charMatrix = [list(line.replace('\n', '').lower()) for line in file.readlines()]

def linearTraverse(matrix, startingPos, offset, toFind = 'xmas') -> bool:
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
        if nextX >= len(matrix[0]) or nextY >= len(matrix) or nextX < 0 or nextY < 0:
            return False
        return linearTraverse(matrix, (nextX, nextY), offset, toFind=toFind[1:])
    return False

foundCount = 0
for y in range(len(charMatrix)):
    for x in range(len(charMatrix[0])):
        startingPos = (x, y)
        foundCount += 1 if linearTraverse(charMatrix, startingPos, (1, 0)) else 0   # E
        foundCount += 1 if linearTraverse(charMatrix, startingPos, (-1, 0)) else 0  # W
        foundCount += 1 if linearTraverse(charMatrix, startingPos, (0, -1)) else 0  # N
        foundCount += 1 if linearTraverse(charMatrix, startingPos, (0, 1)) else 0   # S

        foundCount += 1 if linearTraverse(charMatrix, startingPos, (1, 1)) else 0   # SE
        foundCount += 1 if linearTraverse(charMatrix, startingPos, (1, -1)) else 0  # NE
        foundCount += 1 if linearTraverse(charMatrix, startingPos, (-1, 1)) else 0  # SW  
        foundCount += 1 if linearTraverse(charMatrix, startingPos, (-1, -1)) else 0 # NW
print(f'Found XMAS {foundCount} times')
