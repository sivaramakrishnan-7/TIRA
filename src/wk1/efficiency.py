# implementation 1
import random, time
def count_even(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result


# implementation 2
def count_even1(numbers):
    return sum(x % 2 == 0 for x in numbers)


def efficiency(number):
    print(f"n: {number}")
    numbers = [random.randint(1,10**6) for _ in range(number)]

    start_time = time.time()
    result = count_even(numbers)
    end_time = time.time()

    start_time1 = time.time()
    result1 = count_even1(numbers)
    end_time1 = time.time()

    print("result:", result)
    print("time:", round(end_time - start_time, 2), "s")

    print()

    print("result1:", result1)
    print("time:", round(end_time1 - start_time1, 2), "s")

efficiency(10**7)

