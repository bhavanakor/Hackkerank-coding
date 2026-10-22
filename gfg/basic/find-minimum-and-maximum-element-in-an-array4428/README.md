# Min and Max in Array

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given an array **arr[]**. Your task is to find the  **minimum** and **maximum** elements in the array.

 **Examples:** 

```
Input: arr[] = [1, 4, 3, 5, 8, 6]
Output: [1, 8]
Explanation: minimum and maximum elements of array are 1 and 8.
```

```
Input: arr[] = [12, 3, 15, 7, 9]
Output: [3, 15]
Explanation: minimum and maximum element of array are 3 and 15.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-22T16:53:10.389Z  

```py
class Solution:
    def getMinMax(self, arr):
        ans=[]
        ans.append(min(arr))
        ans.append(max(arr))
        return ans
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/find-minimum-and-maximum-element-in-an-array4428/1)