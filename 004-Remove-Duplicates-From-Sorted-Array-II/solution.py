def remove_duplicates_II(nums):
    i = 2 
    k = 2
    
    while i < len(nums):
        if nums[i] == nums[k - 2]:
            i += 1
        else:
            nums[k] = nums[i]
            i += 1
            k += 1
    return k, nums


print(remove_duplicates_II([1, 1, 1, 2, 2, 3])) #Output must be : 5