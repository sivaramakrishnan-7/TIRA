def sublist(numbers):
    #should contain only 2 distinct integers
    n = len(numbers)
    print(numbers[0:2])
    print(n)
    sub_list = []
    count = 0
    for i in range(n):
        for j in range(i,n):
           curr_sublist =  numbers[i: j+1]
           unique_elements = set(curr_sublist)

           if len(unique_elements) == 2:
                count += 1
                sub_list.append(curr_sublist)
    print(sub_list)
    return count

def sublist_ptr(numbers):
    n = len(numbers)
    a = b = -1 
    for i in range(n):
        

if __name__ == "__main__":
    print(sublist([1,2,3,3,2,2,4,2]))