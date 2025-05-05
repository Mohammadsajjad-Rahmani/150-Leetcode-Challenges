# 🌀 LeetCode 189: Rotate Array

## 📝 Problem Statement

Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

### Example :

```
Input: nums = [1,2,3,4,5,6,7], k = 3  
Output: [5,6,7,1,2,3,4]
```

You may assume `k` is non-negative and that the rotation should be done **in-place** (O(1) extra space) if possible.

---

## 🚀 Approach 1: Using Python Slicing (Not In-Place)

The simplest Pythonic way to rotate the array is using slicing. This method creates a new array by taking the last `k` elements and moving them to the front.

### ✅ Time Complexity: O(n)

### ❌ Space Complexity: O(n) (Not in-place)

```python
def rotate_array(nums, k):
    k = k % len(nums)
    return nums[-k:] + nums[:-k]
```

---

## ⚙️ Approach 2: In-place Rotation Using Reversal (Optimized)

This is an in-place solution that rotates the array using **three reverse operations**:

1. Reverse the entire array
2. Reverse the first `k` elements
3. Reverse the remaining `n-k` elements

### ✅ Time Complexity: O(n)

### ✅ Space Complexity: O(1)

### 🔄 Example:

```
Original:  [1,2,3,4,5,6,7]
Reverse:   [7,6,5,4,3,2,1]
Reverse k: [5,6,7,4,3,2,1]
Final:     [5,6,7,1,2,3,4]
```

### Python Implementation:

```python
def rotate_array_inplace(nums, k):
    k = k % len(nums)

    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    reverse(0, len(nums) - 1)
    reverse(0, k - 1)
    reverse(k, len(nums) - 1)
```

---

## ✅ Key Takeaways

* Always take `k % n` to handle rotations greater than the array size.
* Slicing is easy and clean in Python but not in-place.
* The reverse-in-place method is optimal and commonly asked in interviews.

---

## 🏁 Status

✔ Problem Solved
✔ Slicing approach implemented
✔ In-place approach implemented
