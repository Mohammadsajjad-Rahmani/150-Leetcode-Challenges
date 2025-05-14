### ✅ Problem 7: Best Time to Buy and Sell Stock (Leetcode #121)

**Problem Statement**  
Given an array `prices` where `prices[i]` is the price of a given stock on the ith day, find the maximum profit you can achieve by choosing a single day to buy and another to sell (after the buy day). If no profit is possible, return 0.

---

**Approach: One-Pass Greedy Algorithm**

We iterate through the array once while keeping track of:

- `min_price`: the lowest stock price we've seen so far.
- `max_profit`: the best profit we could have made so far.

At each step:
- If the current price is lower than `min_price`, we update `min_price`.
- Else, we check if selling at this price gives us a better profit than the current `max_profit`.

**Time Complexity:** `O(n)`  
**Space Complexity:** `O(1)`

