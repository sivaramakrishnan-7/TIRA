import time 
def  calculate_efficiency(n):
    my_list = []

    start_add = time.time()
    for i in range(1, n+1):
        my_list.append(i)
    end_add = time.time()

    time_add = end_add - start_add

    print(time_add)

    start_del = time.time()
    for _ in my_list:
        my_list.pop(0)
    end_del = time.time()

    time_del = end_del - start_del

    print(time_del)

if __name__ == "__main__":
    n = 10**5
    calculate_efficiency(n)


