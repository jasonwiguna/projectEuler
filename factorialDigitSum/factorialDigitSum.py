def fact(num):
    if (num == 1):
        return 1
    else:
        return num*fact(num-1)

def digitSum(num):
    if (num < 10):
        return num
    else:
        return num%10 + digitSum(int(num/10))


print(digitSum(fact(int(input()))))