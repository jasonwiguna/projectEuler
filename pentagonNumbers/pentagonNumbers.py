def pentagonNumbers(num):
    return int(num*(3*num-1)/2)

def pentagonPairs():
    pentagonList = []
    found = False
    pentagonList.append(pentagonNumbers(1))
    num = 2
    counter = 2
    while not(found):
        pentagonList.append(pentagonNumbers(num))
        for i in range(1, counter):
            while (pentagonList[counter-1]+pentagonList[i-1] > pentagonList[num-1]):
                num+=1
                pentagonList.append(pentagonNumbers(num))
            if ((pentagonList[counter-1]+pentagonList[i-1]) in pentagonList) and ((pentagonList[counter-1]-pentagonList[i-1]) in pentagonList):
                found = True
                return pentagonList[counter-1]-pentagonList[i-1]
        num += 1
        counter += 1
    return 0

print(pentagonPairs())