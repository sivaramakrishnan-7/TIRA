def max_area(heights):
    left = 0
    right = len(heights) - 1 
    

    while left < right:
        height = min(heights[right],heights[left])
        width  = right - left
        area = width * height

         




