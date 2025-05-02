# Push Dominoes (LeetCode 838)

This repository contains my solution to the [Push Dominoes](https://leetcode.com/problems/push-dominoes/) problem on LeetCode.

## Problem Summary

Given a string representing a line of upright dominoes, some of which are initially pushed to the left ('L') or right ('R'), simulate the final state after all forces have been applied. A domino falling left pushes the adjacent one to the left on the next second, and vice versa. If a domino is pushed from both sides simultaneously, it remains upright.

## Approach

I implemented a **two-pass force simulation** algorithm:
- In the first pass (left to right), simulate the force from falling right ('R') dominoes.
- In the second pass (right to left), simulate the force from falling left ('L') dominoes.
- Then compare the two forces at each position to determine the final state.

## Key Concepts

- String immutability handling in Python.
- Two-directional force simulation.
- Careful state update without mutating the original string.

## File

- `push_dominoes.py`: Python implementation of the solution.

## Status

✅ Accepted on LeetCode  
💡 Written from scratch by myself after understanding the problem deeply and debugging step-by-step.

