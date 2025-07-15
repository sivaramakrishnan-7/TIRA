def mode(numbers):
    count = {}
    mode = numbers[0]

    for x in numbers:
        if x not in count:
            count[x] = 0
        count[x] += 1 
    
        if count[x] > count[mode]:
            mode = x
    return mode

def mode1(numbers):
    mode = (0,0)

if __name__ == "__main__":
    print(mode([1,2,3,2,2,3,2,2]))