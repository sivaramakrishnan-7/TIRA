def count_ways(bits):
    n = len(bits)
    zeros = 0
    result = 0
    for i in range(n):
        if bits[i] == '0':
            zeros += 1
        if bits[i] == '1':
            result += zeros
    return result

def count_ways1(bits):
    n = len(bits)
    result = 0 
    for i in range(n):
        for j in range(i+1,n):
            if bits[i] == '0' and bits[j] == '1':
                result += 1
    return result


if __name__ == "__main__":
    print(count_ways1('01001011'))
