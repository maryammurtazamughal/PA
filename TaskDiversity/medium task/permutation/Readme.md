# Permutations

## Description
Given an array `nums` of distinct integers, this Python code generates all possible permutations of the elements in the array. The result is a list of lists, where each inner list represents a unique permutation of the input elements. The order of the permutations does not matter.

## Solution Explanation
A permutation is a word that describes the number of ways things can be ordered or arranged. To find all possible permutations of a list of distinct integers, we can use the built-in `permutations` function from the `itertools` library.

- The code utilizes the `permutations` function to generate all permutations of the elements in the `nums` array.
- The result is a list of tuples, where each tuple contains a permutation.
- The code then converts each tuple into a list and appends it to the final result list.

## Requirements
To run this code, you need Python 3 installed on your system. The code relies on the `itertools` library, which is part of the Python standard library, so there is no need to install any additional packages.


