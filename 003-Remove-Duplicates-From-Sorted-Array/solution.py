def remove_duplicate(nums):
    i = 1
    k = 1
    
    while i < len(nums):
        if nums[i] != nums[i-1]:
            nums[k] = nums[i]
            i += 1
            k += 1
        else :
            i += 1
    return k

print(remove_duplicate([1,1,2])) # output : 2