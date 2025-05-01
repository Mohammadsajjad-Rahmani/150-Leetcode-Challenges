# Problem: Remove Duplicates from Sorted Array

## Description
Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Return the number of unique elements `k`. The first `k` elements of `nums` should contain the unique values, and the rest of the elements do not matter.

### Example:
```
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
```

```
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
```

## Approach

- Since the array is already sorted, duplicates are guaranteed to be adjacent.
- Use two pointers:
  - `i` to iterate through the array.
  - `k` to track the index of the next unique element's position.
- For each element, if it's not equal to the previous one, copy it to position `k` and increment `k`.
- Return `k` at the end.

## Notes
- ✅ Solved in-place with O(1) extra space.
- ✅ Time complexity is O(n), which is optimal.
- ❗ Initially tried a backwards approach and deleting elements, which was less efficient and made iteration tricky.
- 💡 Realized overwriting duplicates while moving forward is much simpler and faster.
- 🎯 This method is both interview-acceptable and performs well for large arrays.

