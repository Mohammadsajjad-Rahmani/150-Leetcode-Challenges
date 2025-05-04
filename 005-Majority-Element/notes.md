## 🧠 Boyer-Moore Majority Vote Algorithm

### Problem Summary
We are given an array `nums` of size `n`, and we need to find the majority element — the one that appears more than ⌊n/2⌋ times. It is guaranteed that such an element always exists.

---

### Algorithm Idea
The Boyer-Moore Majority Vote algorithm is a brilliant technique for solving this in linear time and constant space.

We treat each element as a vote:
- If two different elements meet, their votes cancel each other out.
- The element with the majority count will survive the cancellation process.

---

### Steps
1. Initialize a `candidate` and a `count` to 0.
2. Iterate over the array:
   - If `count == 0`, assign the current number as the new `candidate`.
   - If the current number equals `candidate`, increment `count`.
   - Otherwise, decrement `count`.
3. The remaining `candidate` is the majority element.

---

