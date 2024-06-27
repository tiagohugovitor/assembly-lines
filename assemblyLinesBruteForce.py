
def assemblyLineBruteForce(S, t, e, x, foundPath):
    n = len(S[0])

    def firstLine(station):
        if station == 0:
            return e[0] + S[0][0]
        keepLineCost = firstLine(station - 1) + S[0][station]
        switchLineCost = secondLine(station - 1) + S[0][station] + t[1][station-1]

        if keepLineCost < switchLineCost:
            return keepLineCost
        return switchLineCost

    def secondLine(station):
        if station == 0:
            return e[1] + S[1][0]
        keepLineCost = secondLine(station - 1) + S[1][station]
        switchLineCost = firstLine(station - 1) + S[1][station] + t[0][station-1]

        if keepLineCost < switchLineCost:
            return keepLineCost
        return switchLineCost
    
    finalFirstLine = x[0] + firstLine(n-1)
    finalSecondLine = x[1] + secondLine(n-1)

    minCost = min(finalFirstLine, finalSecondLine)

    if not foundPath:
        return minCost, []
    
    path = [0] * n
    if minCost == finalFirstLine:
        line = 0
    else:
        line = 1

    for station in range(n - 1, -1, -1):
        path[station] = line
        if line == 0:
            if station == 0:
                break
            if firstLine(station - 1) + S[0][station] <= secondLine(station - 1) + S[1][station] + t[1][station-1]:
                line = 0
            else:
                line = 1
        else:
            if station == 0:
                break
            if secondLine(station - 1) + S[1][station] <= firstLine(station - 1) + S[0][station] + t[0][station-1]:
                line = 1
            else:
                line = 0

    return minCost, path
