# Subtract the Product and Sum of Digits of an Integer

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer number `n`, return the difference between the product of its digits and the sum of its digits.

 

 **Example 1:** 

```
Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2  *3*  4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15

```

 **Example 2:** 

```
Input: n = 4421
Output: 21
Explanation: 
Product of digits = 4  *4*  2 * 1 = 32 
Sum of digits = 4 + 4 + 2 + 1 = 11 
Result = 32 - 11 = 21

```

 

 **Constraints:** 

- 1 <= n <= 10^5

## Solution

**Language:** Python  
**Runtime:** 1 ms (beats 7.41%)  
**Memory:** 19.1 MB (beats 87.53%)  
**Submitted:** 2026-10-23T03:42:12.603Z  

```py
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum=0
        product=1
        while n>0:
            digit=n%10
            sum+=digit
            product*=digit
            n//=10
        return product-sum
        
```

---

[View on LeetCode](https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/)