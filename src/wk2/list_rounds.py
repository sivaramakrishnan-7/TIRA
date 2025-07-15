def find_rounds(numbers):
    #go through the list 
    #find the lowest element
    #put it in collect
    #check if the next lowest element is in the remining list 
    #if its there, put in the collect 
    #check if for next number
    #if it's not there return collect 
    #now start again with full numbers, 
    # exclude one's that are already in collect 
    # start with remaining and repeat the process until full list is completed  

    n = len(numbers)
    if n == 0:
        return []
    
    all_rounds = []
    collected_count = 0
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
    return collected_count


if __name__ == "__main__":
    print(find_rounds([1, 2, 3, 4]))
    # [[1, 2, 3, 4]]

    print(find_rounds([1, 3, 2, 4]))
    # [[1, 2], [3, 4]]    

    print(find_rounds([4, 3, 2, 1]))
    # [[1], [2], [3], [4]]
    
    print(find_rounds([1]))
    # [[1]]

    print(find_rounds([2, 1, 4, 7, 5, 3, 6, 8]))
    # [[1], [2, 3], [4, 5, 6], [7, 8]]
   
    
