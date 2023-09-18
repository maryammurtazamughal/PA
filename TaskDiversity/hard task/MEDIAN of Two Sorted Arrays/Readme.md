# Median of Two Sorted Arrays

## Description

Given two sorted arrays `nums1` and `nums2` of sizes `m` and `n` respectively, this algorithm calculates and returns the median of the two sorted arrays.

## Solution

To solve this problem, we can use the NumPy library in Python, which provides convenient functions for working with arrays and calculating medians:

1. We start by sorting both input arrays, `nums1` and `nums2`, using the `np.sort()` function from NumPy. Sorting is essential to ensure that the arrays are in ascending order.

2. Next, we concatenate the two sorted arrays into a single array using the `np.concatenate()` function. This step combines the two arrays while maintaining the sorted order.

3. Finally, we calculate the median of the concatenated array using the `np.median()` function. The median is the middle value in a sorted array, or the average of the two middle values if the total number of elements is even.

This algorithm leverages the power of NumPy to efficiently sort, concatenate, and calculate the median of the two sorted arrays.

## Example Usage

Here's an example of how to use this algorithm:

```python
import numpy as np

