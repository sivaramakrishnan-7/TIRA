import random,time

def max_diff(numbers):
    result = 0
    for i in numbers:
        for j in numbers:
            result = max(result,abs(i-j))
    return result

def max_diff1(numbers):
    numbers = sorted(numbers)
    result = numbers[-1] - numbers[0]
    return result

def max_diff2(numbers):
    result = max(numbers) - min(numbers)
    return result

print(max_diff([3, 2, 6, 5, 8, 5]))
print(max_diff1([3, 2, 6, 5, 8, 5]))
print(max_diff2([3, 2, 6, 5, 8, 5]))
print()

def calculate_efficiency(n):
    random.seed(1337)

    print(f"n: {n}")
    numbers = [random.randint(1,10**6) for _ in range(n)]
        
    start_time = time.time()
    result = max_diff(numbers)
    end_time = time.time()

    start_time1 = time.time()
    result1 = max_diff1(numbers)
    end_time1 = time.time()

    start_time2 = time.time()
    result2 = max_diff2(numbers)
    end_time2 = time.time()

    print("result:", result)
    print("time:", round(end_time - start_time, 2), "s")

    print()

    print("result1:", result1)
    print("time:", round(end_time1 - start_time1, 2), "s")

    print()

    print("result2:", result2)
    print("time:", round(end_time2 - start_time2, 2), "s")

calculate_efficiency(10000)
print()
calculate_efficiency(1000)