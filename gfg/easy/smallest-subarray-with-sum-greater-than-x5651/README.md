# Smallest Subarray Sum Greater Than x

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a number  **x** and an array of integers  **arr**, find the smallest subarray with sum strictly greater than the given value. If such a subarray do not exist return 0 in that case.

 **Examples:** 

```
Input: x = 51, arr[] = [1, 4, 45, 6, 0, 19]
Output: 3
Explanation: Minimum length subarray is [4, 45, 6]
```

```
Input: x = 100, arr[] = [1, 10, 5, 2, 7]
Output: 0
Explanation: No subarray exist
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-10T04:35:18.752Z  

```py
class Solution:
    def smallestSubWithSum(self, x, arr):
        left=0
        window_sum=0
        min_len=float('inf')
        best_s=float('-inf')
        best_e=float('-inf')
        for right in range(len(arr)):
            window_sum+=arr[right]
            while window_sum>x:
                if right-left+1<min_len:
                    min_len=right-left+1
                    best_s=left
                    best_e=right
                window_sum-=arr[left]
                left+=1
        if min_len==float('inf'):
            return 0
        return min_len
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/smallest-subarray-with-sum-greater-than-x5651/1)