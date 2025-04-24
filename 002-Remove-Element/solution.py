def remove_element(nums, val):
        k = 0  
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i] 
                k += 1
        return k

print(remove_element([3,2,2,3], 3))  # 2