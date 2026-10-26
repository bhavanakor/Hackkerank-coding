# K-th of Two Sorted Arrays

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given two sorted arrays  **a[]** and  **b[]**  and an element  **k**, find the element that would be at the  **kth**  position of the combined sorted array.

 **Examples :** 

```
Input: a[] = [2, 3, 6, 7, 9], b[] = [1, 4, 8, 10], k = 5
Output: 6
Explanation: The final combined sorted array would be [1, 2, 3, 4, 6, 7, 8, 9, 10]. The 5th element of this array is 6.

```

```
Input: a[] = [1, 4, 8, 10, 12], b[] = [5, 7, 11, 15, 17], k = 6
Output: 10
Explanation: Combined sorted array is [1, 4, 5, 7, 8, 10, 11, 12, 15, 17]. The 6th element of this array is 10.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-26T14:01:24.097Z  

```py
class Solution:
    def kthElement(self, a, b, k):
        n, m = len(a), len(b)
        i, j = 0, 0  # Pointers for array 'a' and 'b'
        count = 0    # Tracks the current element index in the combined array

        while i < n and j < m:
            # Pick the smaller element
            if a[i] < b[j]:
                current = a[i]
                i += 1
            else:
                current = b[j]
                j += 1

            count += 1
            if count == k:
                return current

        # If array 'b' is exhausted, pick from 'a'
        while i < n:
            current = a[i]
            i += 1
            count += 1
            if count == k:
                return current

        # If array 'a' is exhausted, pick from 'b'
        while j < m:
            current = b[j]
            j += 1
            count += 1
            if count == k:
                return current

```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1)