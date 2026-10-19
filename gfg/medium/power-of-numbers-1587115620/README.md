# Raise to Power of Its Own Reverse

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a number **n**, find the value of  **n**  raised to the power of its own reverse. The result will always fit into a 32-bit signed integer.

 **Examples:** 

```
Input: n = 2
Output: 4
Explanation: The reverse of 2 is 2, and.
```

```
Input: n = 10
Output: 10
Explanation: The reverse of 10 is 1 (leading zero is discarded), and 10 raised to the power 1 is 10.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-19T15:39:20.541Z  

```py
class Solution:
    def reverseExponentiation(self, n):
        p=str(n)[::-1]
        rev=int(p)
        return pow(n,rev)
        
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/power-of-numbers-1587115620/1)