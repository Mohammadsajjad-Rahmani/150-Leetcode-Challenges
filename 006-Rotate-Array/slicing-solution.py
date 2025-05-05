# This code rotates an array to the right by k steps using slicing.
def rotate_array(nums, k):
    
    k = k % len(nums)  # Handle cases where k is greater than the length of the array
    if k == 0:
        return nums  # No rotation needed
    
    # Rotate the array by slicing
    return nums[-k:] + nums[:-k]

# Example usage
nums = [1,2,3,4,5,6,7]
k = 3
rotated_array = rotate_array(nums, k)
print(f"Rotated array: {rotated_array}")
# Output: Rotated array: [5, 6, 7, 1, 2, 3, 4]
