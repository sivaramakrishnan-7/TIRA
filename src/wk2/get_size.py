import sys 

numbers = []
n = 100
old_size = 0
for i in range(n):
    size = sys.getsizeof(numbers)
    if old_size != size:
        print(len(numbers),size)
        old_size = size
    numbers.append(1)