def validateReport(levels):
    isAscPattern = levels[1] > levels[0]
    for i in range(len(levels)):
        if i == 0:
            continue

        areLevelsEqual = levels[i] == levels[i-1]
        isValidDelta = 1 <= abs(levels[i] - levels[i-1]) <= 3
        isContinuingPattern = (levels[i] > levels[i-1]) == isAscPattern

        if not (isValidDelta and isContinuingPattern and not areLevelsEqual):
            return False

    return True

file = open('part2.txt', 'r')
safeReports = 0
for line in file.readlines():
    report = [int(x) for x in line.split()]
    if validateReport(report):
        safeReports += 1
        continue
    
    for i in range(len(report)):
        tempReport = report.copy()
        tempReport.pop(i)
        if validateReport(tempReport):
            safeReports += 1
            break
    
print(safeReports)


