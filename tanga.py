def tanga(lis1, lis2):
    lis=[3,3]

    for i in range(len(lis1)):
        if lis1[i] == 'share':
            lis[0] -=1
            lis[1] += 3
    for i in range(len(lis2)):
        if lis2[i] == 'share':
            lis[1] -=1
            lis[0] += 3
    return lis

print(tanga(['share', 'share', 'share'], ['steal', 'share', 'steal']))
print(tanga(["share"],["steal"]))