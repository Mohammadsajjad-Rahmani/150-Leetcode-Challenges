## ✅ Problem 7 - Best Time to Buy and Sell Stock II

---

### 📌 Problem Summary

You're given an array `prices` where `prices[i]` is the price of a stock on the *i-th* day.  
You may buy and/or sell the stock on **each** day, but you can **only hold one share at a time**.  
You can even buy and sell on the same day.

**Goal:** Return the **maximum profit** you can achieve by doing multiple transactions (buy/sell).

---

### 🔍 What the Problem Wants

- You **can** buy and sell **multiple times**, even on the same day.
- But you **cannot hold multiple stocks at once** (must sell before buying again).
- Find the **maximum total profit** across all valid transactions.

---

### 🧠 Intuition

Whenever there's a price increase from one day to the next, you can treat it as an opportunity:

> If `prices[i+1] > prices[i]`,  
> buy at `i`, sell at `i+1` → collect `prices[i+1] - prices[i]` profit.

By **adding all such profits**, you get the optimal total — no need to explicitly track buy/sell days.

---

### ✅ Example Walkthrough

**Example 1:**  
Input: `prices = [7,1,5,3,6,4]`  
- Buy at 1, sell at 5 → profit = 4  
- Buy at 3, sell at 6 → profit = 3  
- Total profit = 7

**Example 2:**  
Input: `prices = [1,2,3,4,5]`  
- Buy at 1, sell at 5 → profit = 4  
- Or accumulate 1→2→3→4→5 stepwise: profit = 4

**Example 3:**  
Input: `prices = [7,6,4,3,1]`  
- No profitable transaction → profit = 0

---

### 🔧 Key Notes

- No need to track valleys and peaks.
- Just add **all positive price differences** from day to day.
- Greedy approach: take every opportunity when price goes up.

---

### 💡 Takeaways

- Simple local gains → globally optimal solution.
- Perfect case for greedy logic.
- Don’t overcomplicate — follow the rules and take advantage of allowed moves.
