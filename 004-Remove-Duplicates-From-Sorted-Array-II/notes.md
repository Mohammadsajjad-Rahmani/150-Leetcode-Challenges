## Problem: Remove Duplicates from Sorted Array II

### 📌 Description
Given a sorted array `nums`, modify it in-place such that each unique element appears **at most twice**.  
Return the new length `k`, and ensure the first `k` elements of `nums` reflect the correct result.

### ✅ Constraints
- Array is sorted in non-decreasing order.
- Must be done in-place with O(1) extra memory.

---

### 🧠 Approach
- **Two-pointer technique**:
  - One pointer `i` to iterate through `nums`.
  - Another pointer `k` keeps track of the place to insert the next valid element.
- Start from index 2 because the first two values are always allowed.
- For each element, if it's not equal to `nums[k - 2]`, we can safely place it at `nums[k]`.

---

### 🧩 Example
Input: `[1,1,1,2,2,3]`  
Output: `5`, `nums = [1,1,2,2,3,_]`

---

### 🛠️ Challenges Faced
- Initially confused by how to enforce the "at most twice" condition.
- Early versions either allowed too many duplicates or skipped valid elements.
- Realized the key check is `nums[i] != nums[k - 2]`.

---

### ✅ Final Solution Summary
In-place filtering of duplicates using two pointers, allowing at most two occurrences of each element.
