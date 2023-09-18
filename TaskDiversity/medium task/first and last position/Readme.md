# Find First and Last Position of Element in Sorted Array

## Description
Given an array of integers `nums` sorted in non-decreasing order, this Python code finds the starting and ending position of a given target value in the array.

- If the target is found in the array, it returns a list containing the starting and ending positions.
- If the target is not found in the array, it returns `[-1, -1]`.

## work flow
The code uses a loop to iterate over the `nums` list with the `enumerate` function. The `enumerate` function returns both the iterate value and the index values of the elements in the list.

- It stores the index values in variables `first` and `last`.
- It then uses the `min()` function to find the first index of the target value.
- It uses the `max()` function to find the last index of the target value.

## Requirements
To run this code, you need Python 3 installed on your system. No additional libraries or dependencies are required.

