def isPrime(num):
    if (num == 1):
        return False
    i = 2
    while (i*i <= num):
        if (num % i == 0):
            return False
        i += 1
    return True

def quadraticPrimes():
    aMax = 0
    bMax = 0
    nMax = 0
    n = 0
    for a in range(-1000,1000):
        for b in range(-1000,1000):
            while (isPrime(abs(n*n+a*n+b))):
                n+=1
            if (n > nMax):
                nMax = n
                aMax = a
                bMax = b
            n = 0
    return aMax*bMax

print(quadraticPrimes())