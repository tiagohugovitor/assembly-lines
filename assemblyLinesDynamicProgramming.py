def assemblyLinesDynamicProgrammming(S, t, e, x):
    n = len(S[0])

    F1 = [0] * n
    F2 = [0] * n
    L1 = [0] * n
    L2 = [0] * n
    L1[n-1] = 0
    L2[n-1] = 1

    F1[0] = e[0] + S[0][0]
    F2[0] = e[1] + S[1][0]

    for j in range(1, n):
        keepFirstLineCost = F1[j-1] + S[0][j]
        changeFromSecondLineCost = F2[j-1] + t[1][j-1] + S[0][j]
        if keepFirstLineCost <= changeFromSecondLineCost: 
            F1[j] = keepFirstLineCost
            L1[j-1] = 0
        else:
            F1[j] = changeFromSecondLineCost
            L1[j-1] = 1
        
        keepSecondLineCost = F2[j-1] + S[1][j]
        changeFromFirstLineCost = F1[j-1] + t[0][j-1] + S[1][j]
        if keepSecondLineCost <= changeFromFirstLineCost:
            F2[j] = keepSecondLineCost
            L2[j-1] = 1
        else:
            F2[j] = changeFromFirstLineCost
            L2[j-1] = 0
    if F1[n-1] + x[0] <= F2[n-1] + x[1]:
        finalCost = F1[n-1] + x[0]
        finalL = 0
    else:
        finalCost = F2[n-1] + x[1]
        finalL = 1

    path = L1 if finalL == 0 else L2

    return finalCost, path
