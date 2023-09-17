# Median of Two Sorted Arrays

# Introduction

This Python script calculates the median of two sorted arrays, `nums1` and `nums2`, using a simple algorithm that merges the arrays and finds the median value.

# Problem Description

You are given two sorted arrays, `nums1` and `nums2`. The problem is to find the median of the combined sorted array of these two arrays.

## How the Code Works

The code defines a Python class `Solution` with a method `findMedianSortedArrays(nums1, nums2)` that takes the two sorted arrays as input and returns the median of the combined sorted array. The algorithm involves the following steps:

1. Merge the two input arrays `nums1` and `nums2` into a single list `list`.
2. Sort the merged list in ascending order.
3. Calculate the length of the merged list.
4. If the length is even, find the two middle values and calculate their average to get the median.
5. If the length is odd, simply find the middle value as the median.

## Prerequisites

- Python 3.x is required to run this code.


