import re
file = open('sample.txt', 'r')

def hasSpecialChars(charArr):
    for c in charArr:
        if re.match('[^\\d.]', c) is not None:
            return True
    return False

'''
NOTE THIS IS PRETTY JANK BUT I CBA TO REFACTOR
'''

charMatrix = [list(row.replace('\n', '')) for row in file.readlines()]
rowLength = len(charMatrix[0])
matrixSize = len(charMatrix)
schematic = []
for rowI, row in enumerate(charMatrix):
    startI, endI = None, None
    for charI, char in enumerate(charMatrix[rowI]):
        if startI is None and re.match('\\d', char):
            startI = charI - 1 if charI > 0 else 0
        if startI is not None and endI is None and (re.match('[^\\d]', char) or charI == rowLength - 1):
            endI = charI + 1
        
        if startI != None and endI != None:
            # print(f'{rowI} check range {startI} - {endI}')
            hasSpecialAbove, hasSpecialBellow, hasSpecialInline = False, False, hasSpecialChars(charMatrix[rowI][startI:endI])
            if rowI != 0:
                hasSpecialAbove = hasSpecialChars(charMatrix[rowI - 1][startI:endI])
            if rowI < matrixSize - 1:
                hasSpecialBellow = hasSpecialChars(charMatrix[rowI + 1][startI:endI])
            # print(f'{rowI} {charMatrix[rowI][startI:endI]} {hasSpecialAbove} {hasSpecialInline} {hasSpecialBellow}')

            if hasSpecialAbove or hasSpecialBellow or hasSpecialInline:
                schematicStr = ''
                for c in charMatrix[rowI][startI:endI]:
                    if re.match('\\d', c):
                        schematicStr += c
                schematic.append(int(schematicStr))
            startI, endI = None, None 

print('Schematic',schematic)
print('Sum', sum(schematic))