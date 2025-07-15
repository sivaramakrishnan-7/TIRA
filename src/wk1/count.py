def count_even(numbers):
    count = 0 
    for i in numbers:
        if i%2 == 0:
            count += 1
    return count

def count_even1(numbers):
    return sum(x%2 == 0 for x in numbers)

print(count_even([1,2,3]))
print(count_even([2, 2, 2, 2, 2])) 
print(count_even([5, 4, 1, 7, 9, 6]))

print(count_even1([1,2,3]))
print(count_even1([2, 2, 2, 2, 2])) 
print(count_even1([5, 4, 1, 7, 9, 6]))