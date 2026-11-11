def min_pair_sum(numbers):
    if not numbers:
        return 0
        
    sorted_nums = sorted(numbers)
    total_sum = 0
    left = 0
    right = len(sorted_nums) - 1
    
    while left < right:
        total_sum += sorted_nums[left] * sorted_nums[right]
        left += 1
        right -= 1
        
    return total_sum
