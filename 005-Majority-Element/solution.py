def majority_element(nums):
    count = 0 
    candidate = nums[0]
    
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    
    return candidate
    
    
    
    
    



print(majority_element([2,2,1,1,1,2,2])) # Out put must be : 2