## 🧩 Problem 1: Merge Sorted Array 

**Description:**

You're given two sorted integer arrays `nums1` and `nums2`, and you need to merge `nums2` into `nums1` as one sorted array — in-place.
- `nums1` has enough space at the end to hold all elements of `nums2`.

**Approach Summary:**

- Use two pointers starting from the end of the valid parts of both arrays.
- Compare from the back and insert the larger number at the end of `nums1`.
- Continue until `nums2` is fully merged.

**Challenges Faced:**

- Confused between values in `nums1` that were part of the original input and extra zeroes.
- Tried to access values in `nums1` that had already been overwritten.
- Mistakenly assumed both arrays could be merged in one loop without guarding `nums2` leftovers.

**Key Takeaways:**

- Start merging from the end to avoid overwriting useful data.
- Always check edge cases like: when `nums1` is empty (`m = 0`), or all elements in `nums2` are smaller.
- Two-pointer techniques are powerful for merging sorted structures.
