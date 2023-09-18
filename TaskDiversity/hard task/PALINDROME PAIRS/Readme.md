# Palindrome Pairs

## Description

You are given a 0-indexed array of unique strings `words`. A palindrome pair is defined as a pair of integers `(i, j)` where `i != j`, and the concatenation of the two strings `words[i] + words[j]` is a palindrome. The task is to find and return an array containing all the palindrome pairs of words.

## Solution

A palindrome word is one that reads the same forward and backward. To find palindrome pairs, we can use the following approach:

1. Iterate through the `words` array using two nested loops, with the first loop iterating from 0 to the length of the array.

2. In the inner loop, iterate through the length of the `words` array.

3. For each pair of words, concatenate them and check if the resulting string is a palindrome.

4. To check if a string is a palindrome, you can use negative slicing to reverse the string and then compare it with the original string. If they are equal, it's a palindrome.

5. If the concatenated string is a palindrome, add the pair `(i, j)` to the result.

##Requirement

```python
