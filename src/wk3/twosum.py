def twosum(num, target):
    left = 0
    right = len(num) - 1
    
    while left < right:
        current_sum = num[left] + num[right]
        if current_sum == target:
            return True
        
        if current_sum > target:
            right -= 1
        elif current_sum < target:
            left += 1

    return False
    

if __name__ == "__main__":
    print(twosum([1,3,4,6,8,10,13], 13))

        

