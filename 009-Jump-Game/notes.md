## 🏃‍♂️ Problem: Jump Game

**Category**: Greedy  
**Status**: ✅ Done

---

### 🧠 Problem Statement:

You are given an integer array `nums`. Each element represents your **maximum jump length** at that index.  
Starting from the **first index**, determine if you can reach the **last index**.

---

### 🧪 Examples:

**Example 1:**
Input: nums = [2,3,1,1,4]
Output: True
Explanation:
  - Start at index 0 (value = 2), can jump to 1 or 2.
  - From index 1 (value = 3), can jump directly to the end.

**Example 2:**
Input: nums = [3,2,1,0,4]
Output: False
Explanation:
  - You reach index 3 (value = 0) and cannot go further.


### 💡 Approach: Greedy (Track Maximum Reach)

We maintain a variable `max_reach` to keep track of the **farthest index** we can reach so far.

- Loop through each index `i`:
  - If `i > max_reach`, it means we **cannot** reach this index → return `False`.
  - Otherwise, update `max_reach = max(max_reach, i + nums[i])`.
  - If at any point `max_reach >= len(nums) - 1`, we can reach or pass the last index → return `True`.


