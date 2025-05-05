# Rotate an array to the right by k steps, where k is non-negative.
# This code rotates an array to the right by k steps using in-place reversal.
def rotate_array_inplace(nums, k):
    k = k % len(nums)  # Handle cases where k is greater than the length of the array
    left, right = 0, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    left, right = 0, k - 1
    
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    left, right = k, len(nums) - 1
    
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
        
    return nums  # The array is rotated in place
        

# Example usage
nums = [1,2,3,4,5,6,7]
k = 3
rotated_array = rotate_array_inplace(nums, k)
print(f"Rotated array: {rotated_array}")
# Output: Rotated array: [5, 6, 7, 1, 2, 3, 4]

