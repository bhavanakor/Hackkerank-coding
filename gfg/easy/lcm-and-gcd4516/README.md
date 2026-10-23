# LCM And GCD

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given two integers a and b, You have to compute their LCM and GCD and return an array containing their LCM and GCD.

 **Examples:** 

```
Input: a = 5, b = 10
Output: [10, 5]
Explanation: LCM of 5 and 10 is 10, while their GCD is 5.
```

```
Input: a = 14, b = 8
Output: [56, 2]
Explanation: LCM of 14 and 8 is 56, while their GCD is 2.

```

```
Input: a = 1, b = 1
Output: [1, 1]
Explanation: LCM of 1 and 1 is 1, while their GCD is 1.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-23T05:26:28.157Z  

```py
class Solution:
    def lcmAndGcd(self, a: int, b: int) -> List[int]:
        if a<b:
            l=b
            s=a
        else:
            l=a
            s=b
        while s>0:
            l,s=s,l%s
        gcd=l
        
        lcm=(a*b)//gcd
        
        return [lcm,gcd]
            
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/lcm-and-gcd4516/1)