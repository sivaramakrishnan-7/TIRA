def check_number(number):
    sum = 0 
    values = [3,7,1,3,7,1,3,7]

    if int(number[0]) == 0 and len(number) == 9:
        numberl = list(number)
        str2int = list(map(int,numberl))[:-1]
        for i in range(len(values)):
            sum += values[i] * int(str2int[i])
        diff = (((sum // 10) + 1) * 10) - sum
        if sum % 10 == 0 and int(number[-1]) == 0:
            return True
        elif diff == int(number[-1]):
            return True
        return False
    else:
        return False

if __name__ == "__main__":
    print(check_number("012749138")) # False
    print(check_number("012749139")) # True
    print(check_number("013333337")) # True
    print(check_number("012345678")) # False
    print(check_number("012344550")) # True
    print(check_number("1337")) # False
    print(check_number("0127491390")) # False