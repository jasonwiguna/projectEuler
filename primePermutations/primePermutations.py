def isPrime(num):
    if (num == 1):
        return False
    i = 2
    while (i*i <= num):
        if (num % i == 0):
            return False
        i += 1
    return True

def isPermutation(firstNumber, secondNumber):
    arrDigits = [0]*10
    temp = firstNumber
    while (temp >= 1):
        arrDigits[int(temp%10)]+=1
        temp /= 10
    temp = secondNumber
    while (temp >= 1):
        arrDigits[int(temp%10)]-=1
        temp /= 10
    for i in arrDigits:
        if (i != 0):
            return False
    return True

def findSequence():
    for num in range(1000, 10000):
        if (isPrime(num)) and (num != 1487):
            if (isPrime(num+3330)) and isPermutation(num, num+3330):
                if (isPrime(num+6660)) and isPermutation(num+3330, num+6660):
                    return str(num) + str(num+3330) + str(num+6660)

print(findSequence())