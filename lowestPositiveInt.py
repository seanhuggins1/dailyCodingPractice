

def findLowestPosInt(input):
    upper = 0
    lowestPosInt = 1
    for i in range(len(input)):
        if (input[i] > upper):
            upper = input[i]
        if (input[i] == (lowestPosInt + 1)):
            lowestPosInt += 1
    return lowestPosInt


input = [7,3,0,7,6000,0]


input = [6,2,4,8,3,1,5,9]

9

1


print(findLowestPosInt(input))

