# Array Subset

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given two arrays  **a[]** and  **b[]**, your task is to determine whether  **b[]**  is a subset of  **a[]**.

 **Examples:** 

```
Input: a[] = [11, 7, 1, 13, 21, 3, 7, 3], b[] = [11, 3, 7, 1, 7]
Output: true
Explanation: b[] is a subset of a[]
```

```
Input: a[] = [1, 2, 3, 4, 4, 5, 6], b[] = [1, 2, 4]
Output: true
Explanation: b[] is a subset of a[]
```

```
Input: a[] = [10, 5, 2, 23, 19], b[] = [19, 5, 3]
Output: false
Explanation: b[] is not a subset of a[]
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-23T14:33:10.693Z  

```py
class Solution:
    def isSubset(self, a, b):
        freq={}
        for x in a:
            if x in freq:
                freq[x]+=1
            else:
                freq[x]=1
        
        for x in b:
            if x in freq and freq[x]>0:
                freq[x]-=1
            else:
                return False
        return True
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/array-subset-of-another-array2317/1)