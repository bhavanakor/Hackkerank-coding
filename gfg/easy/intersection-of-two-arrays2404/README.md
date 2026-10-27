# Intersection of Arrays with Distinct

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given two unsorted integer arrays a[] and b[], each consisting of distinct elements, find the intersection (common elements) of the two arrays.

- Returned must contain each common element exactly once.
- The order of elements in the returned array should be same as a[].

 **Examples:** 

```
Input: a[] = [89, 24, 75, 11, 23], b[] = [89, 2, 4]
Output: [89]
Explanation: 89 is the only element in the intersection of the two arrays.
```

```
Input: a[] = [1, 2, 4, 3, 5, 6], b[] = [3, 4, 5, 6, 7]
Output: [4, 3, 5, 6]
Explanation: The common elements are 3, 4, 5, and 6. In a[], they appear in the order 4, 3, 5, 6 (since 4 comes before 3 in a[]), so the result follows that order.
```

```
Input: a[] = [20, 10, 30, 50, 40], b[] = [15, 25, 30, 20, 35]
Output: [20, 30]
Explanation: The common elements are 20 and 30. In a[], 20 appears before 30, so the result is [20, 30].
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-27T06:32:47.358Z  

```py
class Solution:
    def findIntersection(self, a: list[int], b: list[int]) -> list[int]:
        find={}
        result=[]
        for i in range(len(b)):
            find[b[i]]=i
        for j in a:
            if j in find.keys():
                result.append(j)
        return result
                
                
        
                
                
            
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/intersection-of-two-arrays2404/1)