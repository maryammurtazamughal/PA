# Candy Distribution Problem

This Python script solves the candy distribution problem using a greedy algorithm. It calculates the minimum number of candies needed to distribute among students based on their ratings.

## Problem Description

Given an array of student ratings, where ratings[i] represents the rating of the ith student, you need to distribute minimum candies following these rules:
- Each student must have at least one candy.
- Students with a higher rating should get more candies than their neighbors.

## How the Code Works

The code defines a Python class `Solution` with a method `candy(n)` that takes an array `n` as input and returns the minimum number of candies required. It uses a two-pass approach:
1. In the first pass, it compares each student's rating with the one to the left and assigns candies accordingly.
2. In the second pass, it compares each student's rating with the one to the right and updates the candy count if necessary.

## Getting Started

### Prerequisites

- Python 


