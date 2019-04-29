
def findSchedules(workHours, dayHours, pattern):
    totalHours = 0
    result = []
    for c in pattern:
        if c != '?':
            totalHours = totalHours + int(c)

    diff = workHours - totalHours
    constructResult(list(pattern), 0, diff, dayHours, result)
    print(result)


def constructResult(patternArr, index, diff, dayHours, result):
    if index == len(patternArr):
        if diff == 0:
            result.append(''.join(patternArr))
        return

    if patternArr[index] == '?':
        for i in range(0, dayHours+1):
            c = patternArr[index]
            patternArr[index] = str(i)
            constructResult(patternArr, index+1, diff-i, dayHours, result)
            patternArr[index] = c
    else:
        constructResult(patternArr, index+1, diff, dayHours, result)


findSchedules(24, 4, "08??840")
findSchedules(3, 2, "??2??00")
