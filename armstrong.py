def isArmstrong(num):
    number = num
    pow = len(str(num))
    while num:
        number -= (num % 10) ** pow
        num = num // 10

    return True if number == 0 else False

if __name__ == '__main__':
    num = int(input())
    print(isArmstrong(num))
