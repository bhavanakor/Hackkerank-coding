# All Divisors of Number

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer  **n,**  return all the divisors of n in the ascending order.
 
 **Examples:** 

```
Input : n = 20
Output: 1 2 4 5 10 20
Explanation: 20 is completely divisible by 1, 2, 4, 5, 10 and 20.

```

```
Input: n = 21191
Output: 1 21191
Explanation: As 21191 is a prime number, it has only 2 factors(1 and the number itself).
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-23T06:16:03.528Z  

```py
class Solution:
    def getDivisors(self, n):
        divisors=[]
        for i in range(1,int(n**0.5)+1):
            if n%i==0:
                divisors.append(i)
                if i!=n//i:
                    divisors.append(n//i)
        return sorted(divisors)
            
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/all-divisors-of-a-number/1)