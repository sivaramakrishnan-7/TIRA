def count_rounds(numbers):


    initial_state = 1
    

    n = len(numbers)
    if n == 0:
        return []
    
    all_rounds = []
    collected_count = 0
    rounds = 0
    next_to_collect = 1

    while collected_count < n:
        current_round_collected = []

        for num in numbers:
            if num == next_to_collect:
                current_round_collected.append(num)
                collected_count += 1
                next_to_collect += 1

        if current_round_collected:
            all_rounds.append(current_round_collected)
            rounds += 1
    return rounds


if __name__ == "__main__":
    print(count_rounds([1, 2, 3, 4])) # 1
    print(count_rounds([1, 3, 2, 4])) # 2
    print(count_rounds([4, 3, 2, 1])) # 4
    print(count_rounds([1])) # 1
    print(count_rounds([2, 1, 4, 7, 5, 3, 6, 8])) # 4

    n = 10**5
    numbers = list(reversed(range(1, n+1)))
    print(count_rounds(numbers)) # 100000