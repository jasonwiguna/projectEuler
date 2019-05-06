import math

def sumProperDivisors(num):
    if num==1:
        return 1
    n = math.ceil(math.sqrt(num))
    total = 1
    divisor = 2
    while (divisor < n):
        if (num%divisor == 0):
            total += divisor
            total += num//divisor
        divisor+=1
    if n**2==num:
        total+=n
    return total

def isAbundantNumber(num):
    if (sumProperDivisors(num) > num):
        return True
    else:
        return False

def listAbundantNum():
    abundantNumber = []
    for i in range(1, 28124):
        if (isAbundantNumber(i)):
            abundantNumber.append(i)
    return abundantNumber

def nonAbundantSum():
    nonAbundantNum = []
    sums = []
    for i in range(1, 28124):
        nonAbundantNum.append(0)
    abundantNumber = listAbundantNum()
    for i in abundantNumber:
        for j in abundantNumber:
            if (i+j < 28123):
                nonAbundantNum[i+j] = 1
    for i in range(len(nonAbundantNum)):
        if (nonAbundantNum[i]==0):
            sums.append(i)
    return sums

def sumOfNonAbundantNum():
    sums = nonAbundantSum()
    res = 0
    for i in range(len(sums)):
        res += sums[i]
    print(len(sums))
    return res

print(sumOfNonAbundantNum())