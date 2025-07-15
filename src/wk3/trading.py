import random
def best_profit(numbers):
    n = len(numbers)
    best = 0
    for i in range(n):
        for j in range(i+1,n):
            best = max(best, numbers[j] - numbers[i])
    return best

def best_profit1(numbers):
    n = len(numbers)
    best = 0
    for i in range(n):
        min_price = min(numbers[0:i+1])
        best = max(best, numbers[i] - min_price)
    return best

def best_profit2(numbers):
    n = len(numbers)
    best = numbers[0]
    for i in range(n):
        min_price = min(best,numbers[i])
        best = max(best, min_price)
    return best 


while True:
    n = random.randint(1,20)
    prices = [random.randint(1,10) for _ in range(n)]

    result1 = best_profit(prices)
    result2 = best_profit1(prices)
    result3 = best_profit2(prices)

    print(prices,result1,result2,result3)

    if result1 != result3 and result1 != result2 and result2 != result3:
        print("Error")
        break