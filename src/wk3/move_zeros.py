def move(numbers):
    a = 0 
    n = len(numbers)
    for i in range(n):
        if numbers[i] != 0:
            temp = numbers[a]
            numbers[a] = numbers[i]
            numbers[i] = temp
            a += 1 
    return numbers

if __name__ == "__main__":
    print(move([0,1,0,3,12,0]))