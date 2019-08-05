# 42. Maximum Subarray Problem (Kadane's Algorithm)
The following folder contains both an iterative approach as well as a dynamic programming approach to this problem. 

Source: https://www.techiedelight.com/maximum-subarray-problem-kadanes-algorithm/

# Question
Given an array of integers, find the contiguous subarray within it which has the largest sum.

### Input:
```
[-2, 1, -3, 4, -1, 2, 1, -5, 4]
```
### Output:
```
[4, -1, 2, 1] // sum is 6
```

# 5 Steps of Dynamic Programming 
1. Identify the sub-problem
    1. Keeping track of the contiguous segments and to start a new one or build up on the past one
2. Guess first choice
    1. Guess the first index of the given array
3. Recursively define the value of an optimal solution
    1. 
    ```
    Let S(i) be the max sum over all contiguous subsequence ending at i

    Recurrence is defined as:

        a[i], if i = 0
        max{S(i-1) + A[i], A[i]}
    ```
4. Compute the value of an optimal solution (recurse and memoize)
    1. `@recurse`
5. Solve original problem - reconstruct from the sub-problems
    1. Sum
