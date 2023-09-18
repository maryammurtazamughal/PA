# Two Sum

## Description

Given an array of integers `nums` and an integer `target`, this algorithm finds and returns the indices of two numbers in the array such that their sum equals the `target`. The algorithm ensures that each input has exactly one solution, and it does not use the same element twice. The result can be returned in any order.

## Solution

To solve this problem, we use a simple approach:

1. We iterate over the length of the input list `nums` using a for loop.
2. For each iteration, we calculate two values:
   - `A` is obtained by adding the value at the current index `i` to the value at index `0`.
   - `B` is obtained by adding the value at the current index `i` to the value at index `1`.
   - Here, `i` is the loop variable, and `0` and `1` are constants representing the first and second indices in the list.
   - `nums[i]` retrieves the value at the current list index.
3. We then check if the sum of `A` and `B` equals the `target`. If they are equal, it means we have found a pair of numbers that add up to the target.
4. To provide the solution, we use the `index` method to find the indices of the two values in the list that sum to the target.

This simple algorithm guarantees that we find a valid solution in the list `nums` and returns the indices of the two numbers.

